from flask import Flask, render_template, request 
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        N = request.form.get("NAME")
        print(N)

current_datetime = datetime.datetime.now()
print(current_datetime)     