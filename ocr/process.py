from PIL import Image
import pytesseract
import platform
import os
from textblob import TextBlob

# Setup Tesseract path untuk Windows
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)  # pakai 'eng' kalau hasil masih aneh
        return text
    except Exception as e:
        return f"Terjadi error saat proses OCR: {e}"

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "Positif"
    elif polarity < -0.1:
        return "Negatif"
    else:
        return "Netral"
