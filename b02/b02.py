from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", content="Testing")

@app.route("/odd/<num>")
def odd(num):
    return render_template("odd.html", end=10)

@app.route("/list")
def list():
    return render_template("list.html", list=["apple", "banana", "cherry"])

if __name__ == "__main__":
    app.run()