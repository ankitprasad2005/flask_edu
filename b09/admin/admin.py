from flask import Blueprint, render_template

admin = Blueprint("admin", __name__, template_folder="templates", static_folder="static")

@admin.route("/home")
@admin.route("/")
def home():
    return render_template("admin.html")