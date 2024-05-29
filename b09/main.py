from flask import Flask, render_template
from admin.admin import admin

app = Flask(__name__)
app.register_blueprint(admin, url_prefix="/admin")

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)

