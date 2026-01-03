import requests

def test_spam_api():
    response = requests.post(
        "http://localhost:5000/predict",
        json={"message": "Win money now!!!"}
    )
    assert response.status_code == 200
