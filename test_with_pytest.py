import requests

def test_hello_available():
    resp = requests.get("http://127.0.0.1:5000")
    assert resp.status_code == 200

def test_hello_content():
    resp = requests.get("http://127.0.0.1:5000")
    result = resp.json()
    assert result["result"] == "Hello World"