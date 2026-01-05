import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

from src.preprocessing import clean_text
from src.vectorizer import build_vectorizer
import pandas as pd

def main():
    # CSV path
    csv_path = r"C:\Users\kumar\OneDrive\Desktop\Trial2\New-Project\Spam Detection App\data\spam mail.csv"
    df = pd.read_csv(csv_path)
    df.columns = ["label", "message"]

    df["message"] = df["message"].apply(clean_text)
    df["label"] = df["label"].map({"ham": 0, "spam": 1})

    X_train, X_test, y_train, y_test = train_test_split(
        df["message"], df["label"], test_size=0.2, random_state=42
    )

    vectorizer = build_vectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vec, y_train)

    y_pred = model.predict(X_test_vec)
    print(classification_report(y_test, y_pred))

    # SAVE ARTIFACTS (ABSOLUTE PATH)
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ARTIFACTS_PATH = os.path.join(PROJECT_ROOT, "artifacts")
    os.makedirs(ARTIFACTS_PATH, exist_ok=True)

    joblib.dump(model, os.path.join(ARTIFACTS_PATH, "model.pkl"))
    joblib.dump(vectorizer, os.path.join(ARTIFACTS_PATH, "vectorizer.pkl"))

    print("✅ Model and vectorizer saved at:", ARTIFACTS_PATH)


if __name__ == "__main__":
    main()
