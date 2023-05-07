from flask import Flask
from flask_ngrok3 import run_with_ngrok, get_host

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run


@app.route("/")
def hello():
    return "Hello World!"


def get_ngrok_host():
    print(f"ngrok host is: {get_host()}")


app.before_first_request(get_ngrok_host)  # Register function for run before the first request


if __name__ == '__main__':
    app.run()
