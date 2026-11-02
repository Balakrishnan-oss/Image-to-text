"""
Local Image to Text (Offline on CPU) using Salesforce/blip-image-captioning-base.
Lightweight model (~990MB) that runs smoothly on standard laptop CPUs.
"""

import sys
from pathlib import Path
from PIL import Image

def generate_caption(image_path: str) -> str:
    from transformers import BlipProcessor, BlipForConditionalGeneration

    if not Path(image_path).is_file():
        raise FileNotFoundError(f"Image not found at {image_path}")

    model_id = "Salesforce/blip-image-captioning-base"
    print(f"Loading local model '{model_id}' on CPU...")
    processor = BlipProcessor.from_pretrained(model_id)
    model = BlipForConditionalGeneration.from_pretrained(model_id)

    raw_image = Image.open(image_path).convert('RGB')
    inputs = processor(raw_image, return_tensors="pt")

    print("Generating caption...")
    out = model.generate(**inputs, max_new_tokens=50)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python image_to_text_local.py <image_path>")
        sys.exit(1)

    caption = generate_caption(sys.argv[1])
    print("\n--- Generated Caption ---")
    print(caption)
