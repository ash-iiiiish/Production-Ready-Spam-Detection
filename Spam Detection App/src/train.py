import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from data.load_data import load_data
from src.preprocessing import clean_text
from src.vectorizer import build_vectorizer
from data.load_data import load_data

df = load_data("C:/Users/kumar/OneDrive/Desktop/Trial/New-Project/Spam Detection App/data/spam mail.csv")
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

joblib.dump(model, "artifacts/model.pkl")
joblib.dump(vectorizer, "artifacts/vectorizer.pkl")
