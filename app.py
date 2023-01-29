import os

from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")