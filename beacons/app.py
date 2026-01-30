from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, admin!</p>"

current_datetime = datetime.datetime.now()
print(current_datetime)     