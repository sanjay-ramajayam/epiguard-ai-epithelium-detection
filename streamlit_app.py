import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import json
import difflib
import re

# Load model & data
MODEL_PATH = "models/skin_model_final_3.keras"
FAQ_PATH = "data/faq-chatbot-skin.json"

model = tf.keras.models.load_model(MODEL_PATH)

CLASS_NAMES = {
    0: "akiec", 1: "bcc", 2: "bkl", 3: "df", 4: "mel", 5: "nv", 6: "vasc"
}
CLASS_DESC = {
    "akiec": "Actinic Keratoses",
    "bcc": "Basal Cell Carcinoma",
    "bkl": "Benign Keratosis",
    "df": "Dermatofibroma",
    "mel": "Melanoma",
    "nv": "Melanocytic Nevi",
    "vasc": "Vascular Lesion"
}

# Load FAQ data
with open(FAQ_PATH, "r", encoding="utf-8") as f:
    faq_data = json.load(f)

# Function to clean user input for chatbot
def clean_text(text):
    return re.sub(r"[^\w\s]", "", text.lower())

def chatbot_response(user_input):
    cleaned_input = clean_text(user_input)
    if any(bad in cleaned_input for bad in faq_data.get("blacklist", [])):
        return "Tolong gunakan bahasa yang sopan."

    questions = []
    q_to_a = {}
    for cat, qas in faq_data.items():
        if cat == "blacklist": continue
        for qa in qas:
            q_clean = clean_text(qa["question"])
            questions.append(q_clean)
            q_to_a[q_clean] = qa["answer"]

    matches = difflib.get_close_matches(cleaned_input, questions, n=1, cutoff=0.6)
    return q_to_a[matches[0]] if matches else "Maaf, saya belum memahami pertanyaan itu."

# Streamlit UI
st.set_page_config("DermaBot - Deteksi Penyakit Kulit", layout="wide")

# Sidebar (Beranda dan Fitur Pilihan)
with st.sidebar:
    st.image("assets/logo-dermabot.png", caption="DermaBot - Deteksi Penyakit Kulit", use_container_width=True)
    st.title("Selamat Datang di **DermaBot**")

    st.markdown("""
    Aplikasi **DermaBot** dirancang untuk membantu Anda dalam mendeteksi penyakit kulit dan memberikan informasi edukatif mengenai kesehatan kulit.

    🌟 **Fitur-fitur utama DermaBot**:
    - **Deteksi Gambar**: Unggah gambar kulit Anda dan biarkan DermaBot memberikan prediksi mengenai jenis penyakit kulit.
    - **Chatbot FAQ**: Dapatkan informasi terkait penyakit kulit dengan bertanya pada chatbot kami.
    """)

    # Pilihan fitur (menggunakan radio button)
    feature = st.radio("Pilih Fitur", ["📸 Deteksi Gambar", "💬 Tanya Chatbot"])

# Main Content (Tab untuk Deteksi Gambar & Chatbot FAQ)
if feature == "📸 Deteksi Gambar":
    st.title("Deteksi Gambar Penyakit Kulit")
    st.markdown("""
    **Unggah gambar kulit Anda untuk mendeteksi jenis penyakit kulit.**  
    Sistem akan memberikan prediksi berdasarkan gambar yang diunggah.
    """)

    file = st.file_uploader("Pilih gambar (jpg/png)", type=["jpg", "jpeg", "png"])

    if file:
        try:
            # Process image
            img = Image.open(file).convert("RGB").resize((224, 224))
            st.image(img, caption="Gambar yang Diunggah", width=300)

            # Prepare image for prediction
            img_arr = np.expand_dims(np.array(img) / 255.0, axis=0)
            pred = model.predict(img_arr)
            class_id = int(np.argmax(pred))
            confidence = float(np.max(pred))

            class_code = CLASS_NAMES[class_id]
            st.success(f"🧠 Prediksi: {CLASS_DESC[class_code]} (`{class_code}`)")
            st.metric(label="Confidence", value=f"{confidence*100:.2f} %")

            with st.expander("ℹ️ Tentang hasil ini"):
                st.markdown(f"""
                **{CLASS_DESC[class_code]}** adalah jenis penyakit kulit yang dapat dikenali dari ciri-ciri tertentu.  
                Ini hanyalah prediksi awal — silakan konsultasi ke dokter kulit untuk diagnosis resmi.
                """)
        except Exception as e:
            st.error(f"❌ Gagal memproses gambar. Error: {str(e)}")

elif feature == "💬 Tanya Chatbot":
    st.title("Chatbot FAQ Kulit")
    st.markdown("""
    **Tanya seputar penyakit kulit!**  
    Dapatkan informasi melalui chatbot kami yang akan memberikan jawaban atas pertanyaanmu.
    """)

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_question = st.text_input("Tanya sesuatu...")

    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("Kirim") and user_question:
            answer = chatbot_response(user_question)
            st.session_state.chat_history.append((user_question, answer))
    with col2:
        if st.button("🔄 Reset Chat"):
            st.session_state.chat_history = []

    for q, a in reversed(st.session_state.chat_history):
        st.markdown(f"**🧑 Kamu:** {q}")
        st.markdown(f"**🤖 Bot:** {a}")
        st.markdown("---")
