from flask import Flask, render_template, request 
import datetime 
import sqlite3


app = Flask(__name__)
app.config["DATABASE"] = "beacons.db"

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        N = request.form.get("NAME")
        ADDRESS = request.form.get("ADDRESS")
        DAY = request.form.get("day")
        JOB_TYPE = request.form.get("JOB_TYPE")
        return render_template("index.html", N=N,ADDRESS=ADDRESS)

current_datetime = datetime.datetime.now()
print(current_datetime)     