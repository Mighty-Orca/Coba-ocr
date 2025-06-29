from PIL import Image
import pytesseract
import os

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang='ind')  # pakai 'eng' kalau hasil masih aneh
        return text
    except Exception as e:
        return f"Terjadi error saat proses OCR: {e}"
