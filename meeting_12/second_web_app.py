
from flask import Flask, request
import json
app = Flask(__name__)

@app.route("/home")
def hello_world():
    return "Hello, this is the second web app!!! "

@app.route("/greet_user/<user>", methods=["GET"])
def greet(user):
    return f"Hello {user}"

@app.route("/log_message/<msg>", methods=["POST"])
def log_message(msg):
    # req_msg = msg #json.loads(msg)
    with open("log-file.txt", "w") as f :
        f.write(msg)
    return "message written in log"

@app.route("/show_log", methods=["GET"])
def show_log():
    with open("log-file.txt", "r") as f:
        content = f.read()
    return content

if __name__ == "__main__":
    app.run(port=5001)