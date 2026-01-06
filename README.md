# Industrial-Style Spam Detection ML Model

## 📌 Project Overview
This project demonstrates an **industrial-style Machine Learning pipeline** for detecting spam emails.  
It covers data loading, preprocessing, model training, prediction, and deployment via a **Flask web application**, following best practices used in real-world ML systems.

The application allows users to input text and receive a **spam or not-spam prediction** using a trained ML model.

---

## 📂 Project Structure
```
Industrial-Style-ML-Model-Demo-main/
├── Spam Detection App/
│   ├── app/                 # Flask web application
│   ├── src/                 # ML pipeline (training, preprocessing, prediction)
│   ├── data/                # Dataset and data loading scripts
│   ├── artifacts/           # Trained model & vectorizer
│   ├── tests/               # Unit tests
│   ├── Dockerfile           # Docker configuration
│   ├── requirements.txt     # Python dependencies
│   └── README.md
```

---

## 🚀 Features
- End-to-end ML workflow (data → training → inference)
- Spam email classification
- Flask-based web UI
- Modular, production-style codebase
- Dockerized for easy deployment
- Reusable preprocessing and vectorization pipeline

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone <repository-url>
cd Industrial-Style-ML-Model-Demo-main
```

### 2️⃣ Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r "Spam Detection App/requirements.txt"
```

---

## ▶️ Usage

### Run the Flask Application
```bash
cd "Spam Detection App"
python app/app.py
```

Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

---

## 🧠 Machine Learning Pipeline
- **Data Loading**: `data/load_data.py`
- **Preprocessing**: `src/preprocessing.py`
- **Vectorization**: `src/vectorizer.py`
- **Training**: `src/train.py`
- **Prediction**: `src/predict.py`

---

## 🐳 Docker Support
Build and run the application using Docker:

```bash
docker build -t spam-detection-app .
docker run -p 5000:5000 spam-detection-app
```

---

## 🧪 Testing
Run tests from the project root:
```bash
pytest
```

---

## 📦 Dependencies
Key libraries used:
- Flask
- scikit-learn
- pandas
- numpy
- joblib

See `requirements.txt` for the full list.

---

## 🔧 Configuration
Model artifacts are loaded from:
```
Spam Detection App/artifacts/
```

Ensure `model.pkl` and `vectorizer.pkl` are present before running the app.

---

## 📸 Example
Input:
```
Congratulations! You've won a free prize.
```

Output:
```
Spam (High Confidence)
```

---

## 🛠 Troubleshooting
- **Model not found**: Ensure the `artifacts` directory contains trained files.
- **Module errors**: Verify your virtual environment is activated.
- **Port issues**: Make sure port 5000 is free.

---

## 👨‍💻 Contributors
- [@ash-iiiiish](https://github.com/ash-iiiiish)

---

  
