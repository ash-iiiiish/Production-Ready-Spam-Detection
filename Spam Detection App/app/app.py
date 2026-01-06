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
    probability = None

    if request.method == "POST":
        msg = request.form.get("message")   # ✅ SAFE

        if msg and msg.strip():             # ✅ VALIDATION
            msg_vec = vectorizer.transform([msg])
            pred = model.predict(msg_vec)[0]
            prob = model.predict_proba(msg_vec).max()

            prediction = "YES OFCOURSE SPAM" if pred == 1 else "It's NOT SPAM"
            probability = round(prob * 100, 2)

    return render_template(
        "index.html",
        prediction=prediction,
        probability=probability
    )


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    msg = data.get("message", "")

    if not msg.strip():
        return jsonify({"error": "Empty message"}), 400

    msg_vec = vectorizer.transform([msg])
    pred = model.predict(msg_vec)[0]
    prob = model.predict_proba(msg_vec).max()

    return jsonify({
        "prediction": "SPAM" if pred == 1 else "NOT SPAM",
        "confidence": round(prob * 100, 2)
    })


if __name__ == "__main__":
    app.run(debug=True)
