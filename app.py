from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    response = {"key": 1, "value": "test"}
    print(type(response))
    return response


if __name__ == "__main__":
    app.run(debug=True)
