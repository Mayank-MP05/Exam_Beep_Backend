from flask import Flask
from flask_pymongo import PyMongo
import csv

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/weedDB"
mongo = PyMongo(app)


@app.route('/')
def hello():
    return "Hello This is Exam Meet Backend App!"

@app.route("/api/login",methods=["POST"])
def loginHere():
    return

@app.route("/api/signup",methods=["POST"])
def signupHere():
    return

if __name__ == '__main__':
    app.run(debug=True)