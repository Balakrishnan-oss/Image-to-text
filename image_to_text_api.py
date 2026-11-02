"""
Image to Text using Hugging Face Serverless API (Zero local hardware load).
Works great on low-spec laptops because inference runs on the cloud.
"""

import os
import sys
from pathlib import Path
from huggingface_hub import InferenceClient

# Optional: set your token here or as an environment variable HF_TOKEN
HF_TOKEN = os.environ.get("HF_TOKEN", "")

# Lightweight & accurate image-captioning model on Hugging Face
MODEL_ID = "Salesforce/blip-image-captioning-large"

def image_to_text(image_path: str, token: str = None) -> str:
    """Sends an image to Hugging Face and returns a text description."""
    resolved_token = token or HF_TOKEN or None
    client = InferenceClient(api_key=resolved_token)

    if not Path(image_path).is_file():
        raise FileNotFoundError(f"Image file not found: {image_path}")

    print(f"Analyzing '{image_path}' using {MODEL_ID}...")
    caption = client.image_to_text(image_path, model=MODEL_ID)
    return caption

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python image_to_text_api.py <path_to_image>")
        print("Example: python image_to_text_api.py sample.jpg")
        sys.exit(1)

    input_img = sys.argv[1]
    try:
        result = image_to_text(input_img)
        print("\n--- Result Description ---")
        print(result)
    except Exception as e:
        print(f"Error: {e}")
