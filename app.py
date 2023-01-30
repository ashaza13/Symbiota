import os

from flask import Flask, flash, redirect, render_template, request, session, url_for
from logging import FileHandler, WARNING

app = Flask(__name__, template_folder="templates")

file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")