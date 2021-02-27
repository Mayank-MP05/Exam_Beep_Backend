from flask import Flask
from flask_pymongo import PyMongo
import io
import csv

######### Modules Import ######### 
import user_auth

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/weedDB"
mongo = PyMongo(app)


@app.route('/')
def hello():
    return "Hello This is Exam Meet Backend App!"

#################### User Auth ##################

@app.route("/api/login",methods=["POST"])
def loginHere():
    # print("working")
    # print(request)
    data = request.get_json()
    print(data)
    return user_auth.login(data["email"],data["pass1"],data["isCollege"],mongo)

@app.route("/api/signup",methods=["POST"])
def SignupHere():
    # print(request)
    data = request.get_json()
    print(data)
    return user_auth.signup(data["email"],data["pass1"],data["pass2"],data["isCollege"],mongo)  

if __name__ == '__main__':
    app.run(debug=True)