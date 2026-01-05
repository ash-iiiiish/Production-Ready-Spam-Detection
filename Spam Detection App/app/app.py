from flask import Flask, request, jsonify, render_template
import joblib
import os

app = Flask(__name__)

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(PROJECT_ROOT, "artifacts", "model.pkl")
VECTORIZER_PATH = os.path.join(PROJECT_ROOT, "artifacts", "vectorizer.pkl")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        msg = request.form["message"]
        msg_vec = vectorizer.transform([msg])
        pred = model.predict(msg_vec)[0]
        prediction = "spam" if pred == 1 else "ham"
    return render_template("index.html", prediction=prediction)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    msg = data.get("message", "")
    msg_vec = vectorizer.transform([msg])
    pred = model.predict(msg_vec)[0]
    return jsonify({"prediction": "SPAM" if pred == 1 else "NOT SPAM"})

if __name__ == "__main__":
    app.run()
