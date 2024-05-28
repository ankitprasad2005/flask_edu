from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "random_string_key"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["username"]
        passwd = request.form["password"]
        session["user"] = user
        session["passwd"] = passwd
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        usr = session["user"]
        passwd = session["passwd"]
        return f"<h1>{usr} {passwd}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("passwd", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)