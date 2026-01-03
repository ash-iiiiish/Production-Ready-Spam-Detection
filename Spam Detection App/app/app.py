from flask import Flask, request, jsonify
from src.predict import predict_spam

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    message = data.get("message")
    result = predict_spam(message)
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
