"""
Text to Image generation using Hugging Face Free Serverless API.
"""

import os
import sys
from huggingface_hub import InferenceClient

HF_TOKEN = os.environ.get("HF_TOKEN", "")

# High quality and fast model
MODEL_ID = "black-forest-labs/FLUX.1-schnell"

def text_to_image(prompt: str, output_path: str = "output.png", token: str = None):
    resolved_token = token or HF_TOKEN or None
    client = InferenceClient(provider="hf-inference", api_key=resolved_token)

    print(f"Generating image for prompt: '{prompt}'...")
    image = client.text_to_image(prompt, model=MODEL_ID)
    image.save(output_path)
    print(f"Image successfully saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        user_prompt = "A scenic view of a quiet mountain lake at sunrise, highly detailed"
    else:
        user_prompt = " ".join(sys.argv[1:])

    text_to_image(user_prompt)
