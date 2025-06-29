from PIL import Image
import pytesseract
import platform
import os

# Setup Tesseract path untuk Windows
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang='ind')  # pakai 'eng' kalau hasil masih aneh
        return text
    except Exception as e:
        return f"Terjadi error saat proses OCR: {e}"
