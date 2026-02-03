from flask import Flask, render_template, request 
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("index.html")

current_datetime = datetime.datetime.now()
print(current_datetime)     