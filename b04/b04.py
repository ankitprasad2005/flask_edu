from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        passwd = request.form["password"]
        return redirect(url_for("user", usr=user, passwd=passwd))
    else:
        return render_template("login.html")

@app.route("/<usr>/<passwd>")
def user(usr, passwd):
    return f"<h1>{usr} {passwd}</h1>"

if __name__ == "__main__":
    app.run(debug=True)