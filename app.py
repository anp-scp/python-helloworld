from flask import Flask
from flask import jsonify
import logging as log
app = Flask(__name__)
log.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", filename="app.log", level=log.DEBUG)

@app.route("/")
def hello():
    endpoint = "/"
    log.debug("The endpoint: '" + endpoint + "' was reached")
    data = {"result": "Hello World"}
    return jsonify(data), 200

@app.route("/status")
def status():
    endpoint = "/status"
    log.debug("The endpoint: '" + endpoint + "' was reached")
    data = {"result": "OK - healthy"}
    return jsonify(data), 200

@app.route("/metrics")
def metrics():
    endpoint = "/metrics"
    log.debug("The endpoint: '" + endpoint + "' was reached")
    data = {"UserCount": 140, "UserCountActive": 23}
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')
