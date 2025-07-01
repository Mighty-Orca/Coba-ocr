from PIL import Image
import pytesseract
import platform
import os
import joblib

# Setup Tesseract path untuk Windows
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load model sentimen hasil training (.pkl)
model_path = os.path.join("model", "indo_sentimen_model.pkl")  # pastikan path ini benar
sentimen_model = joblib.load(model_path)

# Label map sesuai training
label_map = {
    0: "Negatif",
    1: "Netral",
    2: "Positif"
}

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)  # bisa ditambahkan lang='ind' jika sudah tersedia
        return text
    except Exception as e:
        return f"Terjadi error saat proses OCR: {e}"

def analyze_sentiment(text):
    try:
        pred = sentimen_model.predict([text])[0]
        return label_map.get(pred, "Tidak diketahui")
    except Exception as e:
        return f"Terjadi error saat analisis sentimen: {e}"
