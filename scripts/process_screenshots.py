import os
import time
from scripts.image_to_json import process_image

def process_new_screenshots(screenshots_dir, processed_items_dir):
    """
    Processes new screenshots found in the screenshots directory.
    """
    while True:
        for filename in os.listdir(screenshots_dir):
            if filename.endswith((".png", ".jpg", ".jpeg")):  # Add other extensions if needed
                image_path = os.path.join(screenshots_dir, filename)
                # Process the image using the modified process_image function
                process_image(image_path, processed_items_dir)

        # Wait for a while before checking again
        time.sleep(60)  # Check for new screenshots every 60 seconds (adjust as needed)

if __name__ == "__main__":
    SCREENSHOTS_DIR = "screenshots"  # Directory where you drop screenshots
    PROCESSED_ITEMS_DIR = "data/processed_items"  # Directory where processed items are stored
    process_new_screenshots(SCREENSHOTS_DIR, PROCESSED_ITEMS_DIR)
