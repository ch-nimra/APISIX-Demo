from flask import Flask

app = Flask(__name__)

@app.route("/django/")
def hello_world():
    return "<p>Hello, Django!</p>"

if __name__ == "__main__":
    app.run(debug=True)