from flask import Flask,request,render_template
from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask_pymongo import PyMongo
import io
import csv

######### Modules Import ######### 
import user_auth
import uploaders

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/weedDB"
app.config['UPLOAD_FOLDER'] = "files_here/"

mongo = PyMongo(app)

#################### DEMO ######################
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

################ Uploader Functions ########################
@app.route('/api/upload', methods=["POST"])
def uploadData():
    # print(request)
    # print(request.form)
    # print(request.files)
    file = request.files["fileToBeUploaded"]
    data = request.get_json()
    # print(request.files["collection"])
    coll = request.form["collection"]
    return uploaders.upload(file,coll,mongo)


if __name__ == '__main__':
    app.run(debug=True)