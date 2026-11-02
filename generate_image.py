import io
import urllib.parse
import urllib.request
from PIL import Image
from huggingface_hub import InferenceClient

# 1. Your Hugging Face token (set via environment variable or paste here)
HF_TOKEN = os.environ.get("HF_TOKEN", "")

# 2. Pick a model
MODEL_ID = "black-forest-labs/FLUX.1-schnell"

# 3. Enter your prompt
prompt = "An adorable cute fluffy kitten with big expressive round eyes, ultra-detailed soft fur, whiskers, 4K resolution, studio lighting, highly realistic"

output_filename = "output.png"

print(f"Generating image for prompt: '{prompt}'...")

# Try Hugging Face first
try:
    client = InferenceClient(api_key=HF_TOKEN)
    image = client.text_to_image(prompt, model=MODEL_ID)
    image.save(output_filename)
    print(f"Done! Image generated via Hugging Face and saved to {output_filename}")

except Exception as hf_err:
    # Hugging Face recently transitioned free serverless diffusion to paid third-party
    # inference providers (returning 402 Payment Required or 410 Gone).
    print(f"\n[Notice] Hugging Face serverless provider returned: {hf_err}")
    print("Switching to free open-access FLUX endpoint (no credits required)...")
    
    encoded_prompt = urllib.parse.quote(prompt)
    free_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?model=flux"
    
    urllib.request.urlretrieve(free_url, output_filename)
    print(f"Done! Image generated via FLUX and saved to {output_filename}")
