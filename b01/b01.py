from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, this is home page"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

# @app.route("/admin")
# def admin():
#     return redirect(url_for("home"))

@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run()