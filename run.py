import os
from flask import Flask, render_template, request, flash, url_for


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


app.run(host=os.environ.get("IP", "0.0.0.0"), port=int(os.environ.get("PORT", "5000")), debug=True)