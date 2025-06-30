import streamlit as st
import os
from ocr.process import extract_text_from_image, analyze_sentiment
from PIL import Image

# Folder upload
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.title("📄 Media Monitoring OCR")

uploaded_file = st.file_uploader("Upload screenshot berita (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Simpan file
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"Berhasil upload: {uploaded_file.name}")

    # Tampilkan gambar
    st.image(Image.open(file_path), caption="Gambar Berita", use_container_width=True)

    # Tombol proses OCR
    if st.button("🔍 Scan OCR"):
        with st.spinner("Sedang memproses gambar..."):
            extracted_text = extract_text_from_image(file_path)
            st.session_state.extracted_text = extracted_text
            # reset sentimen kalau OCR baru
            st.session_state.pop("sentimen", None)

# Tampilkan teks hasil OCR kalau sudah ada
if "extracted_text" in st.session_state:
    st.subheader("📝 Hasil OCR:")
    st.text_area("Teks yang Terdeteksi:", st.session_state.extracted_text, height=300)

    # Tombol analisis sentimen
    if st.button("🔎 Analisis Sentimen"):
        with st.spinner("Sedang menganalisis sentimen..."):
            sentimen = analyze_sentiment(st.session_state.extracted_text)
            st.session_state.sentimen = sentimen

# Tampilkan hasil sentimen kalau sudah dianalisis
if "sentimen" in st.session_state:
    emoji = {
        "Positif": "🟢",
        "Netral": "🟡",
        "Negatif": "🔴"
    }
    st.subheader("📊 Hasil Sentimen:")
    st.markdown(f"**Sentimen Artikel:** {emoji[st.session_state.sentimen]} {st.session_state.sentimen}")
