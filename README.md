# 🧠 DermaBot - Skin Disease Detection & FAQ Chatbot

**DermaBot** adalah aplikasi web berbasis kecerdasan buatan (AI) yang dirancang untuk membantu deteksi penyakit kulit dari gambar serta menyediakan chatbot edukatif untuk menjawab pertanyaan seputar kesehatan kulit.

Aplikasi ini dibangun menggunakan model **MobileNetV2** untuk klasifikasi gambar dan **difflib** untuk chatbot berbasis text similarity dan rule-based.

---

## 📌 Fitur Utama

- 🔍 **Deteksi Penyakit Kulit**: Prediksi 7 jenis penyakit kulit dari gambar.
- 💬 **Chatbot Edukasi**: Jawaban otomatis untuk pertanyaan umum seputar kulit.
- 📊 **Evaluasi Model**: Akurasi validasi hingga **74%**, visualisasi metrik lengkap.
- 🌐 **Web App Interaktif**: Dibangun dengan Streamlit, sangat user friendly.

---

## 📁 Dataset

Dataset yang digunakan adalah **HAM10000** (Human Against Machine with 10000 training images), free di Kaggle:

🔗 [HAM10000 - Kaggle](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000)

---

## ⚙️ Tech Stack

| Komponen        | Teknologi yang Digunakan                |
|-----------------|------------------------------------------|
| Model Deteksi   | TensorFlow, Keras, MobileNetV2           |
| Dataset         | HAM10000 (Kaggle)                        |
| Preprocessing   | NumPy, PIL, OpenCV                       |
| Evaluasi        | Scikit-learn, Matplotlib, Seaborn        |
| Web App         | Streamlit                                |
| Chatbot         | difflib (SequenceMatcher)                |
| Deployment      | Lokal / Streamlit Cloud                  |
| Version Control | Git, GitHub                              |

---

## 🚀 Cara Menjalankan

### 1. Clone Repository
```bash
git clone https://github.com/Nanaacaw/skin_disease_prediction.git
cd skin_disease_prediction
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi
```bash
streamlit run streamlit_app.py
```

---

## 🧪 Evaluasi Model

- Akurasi validasi: **74%**
- Visualisasi training:
  - Kurva Akurasi & Loss
  - Classification Report
  - Confusion Matrix

---

## 🗂️ Struktur Folder

```
SKIN_DISEASE_DETECTION/
├── assets/                       # Asset tambahan (gambar, icon, dll)
├── data/                         # Data & file pendukung
│   ├── images/                   # Folder untuk gambar input (download dataset terlebih dahulu)
│   ├── faq-chatbot-skin.json     # Data chatbot FAQ
│   └── HAM10000_metadata.csv     # Metadata dari dataset HAM10000
├── models/
│   └── skin_model_final_3.keras  # Model CNN hasil training
├── notebooks/                    # Notebook untuk eksplorasi dan training
│   ├── training.ipynb
│   └── training_fix.ipynb
├── streamlit_app.py              # Aplikasi utama berbasis Streamlit
├── requirement.txt               # Daftar library yang dibutuhkan
└── .gitignore
```

---

## 📖 Lisensi

Proyek ini dilisensikan di bawah MIT License - silakan gunakan, modifikasi, dan kembangkan untuk kepentingan edukasi dan penelitian.

---

## 📫 Contact Me

If you have any suggestions or feedback, please don't hesitate to contact to me in direct message on ::

- 📧 Email: [awnana123@gmail.com](mailto:awnana123@gmail.com)
- 💼 LinkedIn: [https://linkedin.com/in/nana-caw](https://linkedin.com/in/nana-caw)


