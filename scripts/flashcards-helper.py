import requests
import json
from google import genai
from google.genai import types

ANKI_CONNECT_URL = "http://localhost:8765"

client = genai.Client()

def get_word_details(word):
    # prompt = f"""
    # You are a German linguistics expert. Analyze the word: "{word}", and return 3 JSON fields, namely "translation", "line1" and "line2".
    
    # 1. For the field "translation", provide the most common English or Arabic translation along side the definite article. Example: "the table" or "الطاولة".
    
    # 2. For the field "line1", If the word is a noun, then find the article for this word and the plural form (e.g., "der Tisch, die Tische"). If the word is a verb, an adjective or a preposition, then just the word itself.
    
    # 3. For the field "line2", If the word is a verb, then provide the indicative (Präsens, Präteritum, Perfekt), the konjunktiv (Konjunktiv I, Konjunktiv II Präsens, Konjunktiv II Perfekt) and a small example sentence. If the word is an adjective, then provide the Comparative and superlative forms, along with a small example sentence. If the word is a noun or a preposition, then provide only a small example sentence.
    # """

    prompt = f"""
    You are a German linguistics expert. Analyze the word: "{word}".

    Return ONLY a JSON object:
    {{
      "translation": "An English or Arabic of the word according to the rules below",
      "line1": "The word, with additional info as per the rules below",
      "line2": "Additional details as per the rules below"
    }}
    
    RULES:
    1. Field "translation":
       - Provide the most common English or Arabic translation along side the definite article. Example: "the table" or "الطاولة".
       - The translation MUST NOT contain any German words.
    
    2. Field "line1":
       - If the word is a noun, then find the article for this word and the plural form (e.g., "der Tisch, die Tische").
       - If the word is a verb, an adjective or a preposition, then just the word itself.
    
    3. Field "line2":
       - If the word is a verb, then provide exactly 3 lines:
          - Indicative verb stem without ending (Präsens, Präteritum, Perfekt)
          - Konjunktiv verb stem without ending (Konjunktiv I, Konjunktiv II Präsens, Konjunktiv II Perfekt)
          - Example Sentence
       - If the word is an adjective, then provide 2 lines:
         - The Comparative, Superlative forms. Example: "schneller, am schnellsten".
         - An Example Sentence
       - If the word is a noun or a preposition: Example Sentence only
    """
    
    try:
        response = client.models.generate_content(
            # model='gemini-2.5-flash',
            model="gemini-3-flash-preview",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type='application/json',
            )
        )
        non_raw_response = json.loads(response.text)
        return non_raw_response
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
        return None

def add_to_anki(data):
    # Fix: Handle the backslash replacement OUTSIDE the f-string
    formatted_line2 = data['line2'].replace('\n', '<br>')
    
    note = {
        "deckName": "Vom Unterricht", 
        "modelName": "Basic",
        "fields": {
            "Front": data['translation'],
            "Back": f"<b>{data['line1']}</b><br><div style='font-size: 0.9em; margin-top: 5px;'>{formatted_line2}</div>"
        },
        "options": {"allowDuplicate": False}
    }
    res = requests.post(ANKI_CONNECT_URL, json={"action": "addNote", "version": 6, "params": {"note": note}})
    return res.json()

# Main Loop Logic
with open("words.txt", "r") as f:
    for word in f.readlines():
        word = word.strip()
        if not word: continue
        
        print(f"\n--- Analyzing: {word} ---")
        details = get_word_details(word)
        
        if details:
            print(f"Front: {details['translation']}")
            print(f"Back L1: {details['line1']}")
            print(f"Back L2: {details['line2']}")
            
            choice = input("\n[Enter] Add | [n] Skip | [e] Edit: ").lower()
            if choice == '':
                add_to_anki(details)
                print("Added to Anki.")
            elif choice == 'e':
                details['translation'] = input("New Translation: ") or details['translation']
                add_to_anki(details)
                print("Edited and Added.")