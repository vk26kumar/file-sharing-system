from flask import Flask, render_template, request, send_from_directory, redirect, session
import os

app = Flask(__name__)
app.secret_key = "securekey123"
PASSWORD = "12345"
FILES_DIR = "files"

if not os.path.exists(FILES_DIR):
    os.makedirs(FILES_DIR)

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        if request.form["password"] == PASSWORD:
            session["logged"] = True
            return redirect("/home")
    return render_template("login.html")

@app.route("/home")
def home():
    if "logged" not in session: return redirect("/")
    files = os.listdir(FILES_DIR)
    return render_template("index.html", files=files)

@app.route("/download/<path:filename>")
def download(filename):
    if "logged" not in session: return redirect("/")
    return send_from_directory(FILES_DIR, filename, as_attachment=True)

@app.route("/upload", methods=["POST"])
def upload():
    if "logged" not in session: return redirect("/")
    file = request.files["file"]
    file.save(os.path.join(FILES_DIR, file.filename))
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
