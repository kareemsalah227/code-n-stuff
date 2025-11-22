#!/bin/bash

# Define the target quality level for FFmpeg (1=best, 31=worst)
# A value of 8 to 10 is usually a good compromise for high visual quality.
FFMPEG_QUALITY=8

echo "Starting JPG image quality reduction using FFmpeg (Quality: $FFMPEG_QUALITY)..."
echo "---"

# Loop through all files ending in .jpg or .jpeg (case-insensitive) in the current directory
find . -maxdepth 1 -type f \( -iname "*.jpg" -o -iname "*.jpeg" \) | while IFS= read -r file; do
    # Get the base filename (e.g., "photo.jpg")
    filename=$(basename "$file")
    
    # Create the new filename with a "_small" suffix (e.g., "photo_small.jpg")
    new_filename="${filename%.*}_small.${filename##*.}"
    
    # Use ffmpeg to reduce the quality
    # -i: input file
    # -q:v: sets the quality scale (1=best, 31=worst)
    # -y: automatically overwrite the output file if it exists (for safe re-runs)
    
    if ffmpeg -i "$file" -q:v "$FFMPEG_QUALITY" -y "$new_filename" > /dev/null 2>&1; then
        # Get and display the file sizes for comparison
        # Note: 'du -h' or 'ls -lh' is used for human-readable size, but may not be precise for scripting
        original_size=$(du -h "$file" | cut -f1)
        new_size=$(du -h "$new_filename" | cut -f1)
        
        echo "✅ Processed: $filename"
        echo "   Original Size: $original_size -> New Size: $new_size"
    else
        echo "❌ FAILED to process: $filename (Check FFmpeg installation/errors)"
    fi
    
    echo "---"
done

echo "Script finished."
