# Image to Text (and Text to Image) Project

This project provides ready-to-run scripts tailored for low-spec or government laptops using Hugging Face AI models.

---

## 📁 Project Structure

- `image_to_text_api.py`: **Image to Text (Cloud / Recommended)** — Takes an image and describes what's in it using Hugging Face's free cloud server (0% CPU/RAM strain).
- `image_to_text_local.py`: **Image to Text (Offline Local CPU)** — Uses a lightweight local model (`Salesforce/blip-image-captioning-base`) if your laptop has no internet.
- `text_to_image.py`: **Text to Image (Cloud)** — Generates an image from a text prompt.
- `requirements.txt`: Python package dependencies.

---

## 🚀 Quick Setup

### 1. Install Dependencies
Open your terminal in this folder and run:
```bash
pip install -r requirements.txt
```

*(For local offline mode only, you will also need: `pip install torch torchvision transformers`)*

### 2. Set Up Hugging Face Token (Free)
1. Get a free token at [Hugging Face Settings](https://huggingface.co/settings/tokens).
2. Set it in your terminal:
   - **PowerShell**: `$env:HF_TOKEN = "your_token_here"`
   - **Command Prompt**: `set HF_TOKEN=your_token_here`
   - Or paste it directly inside `image_to_text_api.py`.

---

## 💡 How to Run

### Describe an Image (Image to Text via Cloud):
```bash
python image_to_text_api.py sample.jpg
```

### Describe an Image (Offline on CPU):
```bash
python image_to_text_local.py sample.jpg
```

### Generate an Image from Text:
```bash
python text_to_image.py "A serene landscape with mountains and lake at sunset"
```
