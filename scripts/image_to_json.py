import pytesseract
import cv2
import json
import re
import os
from utils import generate_item_hash

def extract_text_from_image(image_path):
    # ... (same as before) ...

def parse_item_data(text):
    # ... (same as before) ...

def process_image(image_path, output_dir="data/processed_items"):
    """
    Extracts item data from an image, generates a hash, and saves it as a JSON file.
    """
    extracted_text = extract_text_from_image(image_path)
    if extracted_text:
        item_data = parse_item_data(extracted_text)
        if item_data:
            # Generate the hash for the item
            item_hash = generate_item_hash(item_data)
            item_data["Hash"] = item_hash

            # Create a unique filename using the hash
            output_filename = os.path.join(output_dir, f"{item_hash}.json")

            # Ensure the output directory exists
            os.makedirs(output_dir, exist_ok=True)

            # Save the item data to a new JSON file
            with open(output_filename, "w") as f:
                json.dump(item_data, f, indent=4)

            print(f"Item data from {image_path} saved to {output_filename}")
        else:
            print(f"Failed to parse item data from {image_path}.")
    else:
        print(f"Failed to extract text from {image_path}.")

if __name__ == "__main__":
    image_path = input("Enter the path to the item screenshot: ")
    process_image(image_path)

