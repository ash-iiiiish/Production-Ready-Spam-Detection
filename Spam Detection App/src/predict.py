import joblib
from src.preprocessing import clean_text

model = joblib.load("artifacts/model.pkl")
vectorizer = joblib.load("artifacts/vectorizer.pkl")

def predict_spam(text):
    cleaned = clean_text(text)
    vector = vectorizer.transform([cleaned])
    pred = model.predict(vector)[0]
    return "Spam" if pred == 1 else "Not Spam"
