from flask import Flask, redirect, url_for, render_template, request, session, flash
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
        flash("Login successful!", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!", "info")
            return redirect(url_for("user"))
        flash("You are not logged in.", "info")
        flash("Please login to continue!", "info")
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        usr = session["user"]
        passwd = session["passwd"]
        return render_template("user.html", user=usr, passwd=passwd)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"You have been logged out, {user}!", "info")
    session.pop("user", None)
    session.pop("passwd", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)