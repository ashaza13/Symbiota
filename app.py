import os

from flask import Flask, flash, redirect, render_template, request, session, url_for
from logging import FileHandler, WARNING
from authentication import process_login, process_create
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__, template_folder="templates")
app.secret_key = "chicken_nugs"

file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        token = process_login(email, password)

        if token == None:
            print("here")
        # if not request.form.get("email"):
        #     # add an alert
        # elif not request.form.get("password"):
        #     # add an alert
        session["user_id"] = token
        return redirect("/")
    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # if password != request.form.get("confirmation"):


        process_create(email, password)
        # if not request.form.get("email"):
        #     # add an alert
        # elif not request.form.get("password"):
        #     # add an alert
        return redirect("/")
    else:
        return render_template("register.html")