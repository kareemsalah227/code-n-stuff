import requests
import json
import os
import argparse
from google import genai
from google.genai import types

# Configuration
INPUT_FILE = "sentences.txt"
ANKI_CONNECT_URL = "http://localhost:8765"
ANKI_DECK_NAME = "Sätze"

client = genai.Client()

def get_sentence_details(sentence):
    """Uses AI to analyze the German sentence and provide translations and examples."""
    prompt = f"""
    You are a German language tutor. Analyze the following German sentence or expression: "{sentence}".

    Return ONLY a JSON object:
    {{
      "english_meaning": "The natural English meaning (not literal). If there are multiple contextual meanings, provide each on a new line.",
      "german_original": "{sentence}",
      "examples": "One or two simple, easy B1-level example sentences. Put each example on a new line."
    }}
    
    RULES:
    1. "english_meaning": Focus on how a native speaker would say this in English. Use a new line for each distinct meaning or nuance.
    2. "german_original": Keep the sentence exactly as provided.
    3. "examples": Must be clear, short, and appropriate for B1 level. Provide one or two sentences, each on its own line.
    """

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt,
            config=types.GenerateContentConfig(
                # Ensure the model returns valid JSON
                response_mime_type="application/json",
            ),
        )
        return json.loads(response.text)
    except Exception as e:
        print(f"Error calling AI: {e}")
        return None

def add_to_anki(data):
    """Sends the formatted data to Anki via AnkiConnect."""
    # Convert Python newlines (\n) to HTML breaks (<br>) for Anki
    formatted_front = data["english_meaning"].replace("\n", "<br>")
    formatted_examples = data["examples"].replace("\n", "<br>")
    
    note = {
        "deckName": ANKI_DECK_NAME,
        "modelName": "Basic",
        "fields": {
            "Front": formatted_front,
            "Back": f"<b>{data['german_original']}</b><hr><div style='font-size: 0.85em; color: #555;'>{formatted_examples}</div>",
        },
        "options": {"allowDuplicate": False},
    }
    
    try:
        res = requests.post(
            ANKI_CONNECT_URL,
            json={"action": "addNote", "version": 6, "params": {"note": note}},
        )
        return res.json()
    except Exception as e:
        print(f"Error connecting to Anki: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="German Sentence Flashcards Helper")
    parser.add_argument(
        "--skip-review",
        action="store_true",
        help="Add directly to Anki without manual approval",
    )
    args = parser.parse_args()

    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    for sentence in lines:
        print(f"\n" + "="*30)
        print(f"Processing: {sentence}")

        details = get_sentence_details(sentence)

        if details:
            print(f"Front (Meaning):\n{details['english_meaning']}")
            print(f"Back (German): {details['german_original']}")
            print(f"Back (Examples):\n{details['examples']}")

            if args.skip_review:
                add_to_anki(details)
                print("Result: Added to Anki.")
            else:
                choice = input("\n[Enter] Add | [n] Skip | [e] Edit Meaning: ").lower()
                if choice == "":
                    add_to_anki(details)
                    print("Result: Added to Anki.")
                elif choice == "e":
                    details["english_meaning"] = input("Enter custom meaning: ") or details["english_meaning"]
                    add_to_anki(details)
                    print("Result: Edited and Added.")
                else:
                    print("Result: Skipped.")

    print(f"\n✨ Done!")

if __name__ == "__main__":
    main()