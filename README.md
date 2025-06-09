# 🧠 **EPIGAURD AI - Epithelium Detection** - Skin Disease Detection & FAQ Chatbot

**EPIGAURD AI** is an AI-powered web application designed to help detect epithelium-related skin diseases from images and provide an educational chatbot to answer common questions related to skin health.

This app is built using the **MobileNetV2** model for image classification and **difflib** for a text similarity and rule-based chatbot.

---

## 📌 Key Features

* 🔍 **Skin Disease Detection**: Predicts 7 types of skin diseases from images.
* 💬 **Educational Chatbot**: Automatically answers common questions about skin health.
* 📊 **Model Evaluation**: Validation accuracy up to **74%**, with full metric visualization.
* 🌐 **Interactive Web App**: Built with Streamlit, highly user-friendly.

---

## 📁 Dataset

The dataset used is **HAM10000** (Human Against Machine with 10,000 training images), available for free on Kaggle:

🔗 [HAM10000 - Kaggle](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000)

---

## ⚙️ Tech Stack

| Component       | Technologies Used                 |
| --------------- | --------------------------------- |
| Detection Model | TensorFlow, Keras, MobileNetV2    |
| Dataset         | HAM10000 (Kaggle)                 |
| Preprocessing   | NumPy, PIL, OpenCV                |
| Evaluation      | Scikit-learn, Matplotlib, Seaborn |
| Web App         | Streamlit                         |
| Chatbot         | difflib (SequenceMatcher)         |
| Deployment      | Local / Streamlit Cloud           |
| Version Control | Git, GitHub                       |

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Nanaacaw/skin_disease_prediction.git
cd skin_disease_prediction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run streamlit_app.py
```

---

## 🧪 Model Evaluation

* Validation accuracy: **74%**
* Training visualizations:

  * Accuracy & Loss Curves
  * Classification Report
  * Confusion Matrix

---

## 🗂️ Folder Structure

```
SKIN_DISEASE_DETECTION/
├── assets/                       # Additional assets (images, icons, etc.)
├── data/                         # Supporting data & files
│   ├── images/                   # Input image folder (download dataset first)
│   ├── faq-chatbot-skin.json     # FAQ chatbot data
│   └── HAM10000_metadata.csv     # HAM10000 dataset metadata
├── models/
│   └── skin_model_final_3.keras  # Trained CNN model
├── notebooks/                    # Notebooks for exploration and training
│   ├── training.ipynb
│   └── training_fix.ipynb
├── streamlit_app.py              # Main Streamlit web application
├── requirement.txt               # Required libraries
└── .gitignore
```

---

## 📖 License

This project is licensed under the MIT License — feel free to use, modify, and expand it for educational or research purposes.
