from flask import Flask,request,render_template
from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask_pymongo import PyMongo
import io
import csv

######### Modules Import ######### 
import user_auth
import uploaders
import user_side_queries
import college_side_queries
import profile_updater

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
    # return user_auth.login(data["email"],data["pass1"],data["isCollege"],mongo)
    return user_auth.login(data["email"],data["pass1"],mongo)

@app.route("/api/signup",methods=["POST"])
def SignupHere():
    # print(request)
    data = request.get_json()
    print(data)
    # return user_auth.signup(data["email"],data["pass1"],data["pass2"],data["isCollege"],mongo)  
    return user_auth.signup(data["email"],data["name"],data["pass1"],data["pass2"],mongo)  

################ Uploader Functions ########################
@app.route('/api/upload', methods=["POST"])
def uploadData():
    # print(request)
    # print(request.form)
    # print(request.files)
    file = request.files["fileToBeUploaded"]
    # data = request.get_json()
    # print(request.files["collection"])
    coll = request.form["collection"]
    return uploaders.upload(file,coll,mongo)

################### User PRN updater #######################
@app.route('/api/userUpdation', methods=["POST"])
def userUpdation():
    data = request.get_json()
    return profile_updater.updateProfile(data["email"],data["prn_no"],data["clg_id"],mongo)

################## Get User Profile ####################
@app.route('/api/getUserProfile', methods=["POST"])
def getProfileDetails():
    data = request.get_json()
    return profile_updater.getProfileFromStuds(data["email"],mongo)

@app.route('/api/getUserCollegeProfile', methods=["POST"])
def getClgProfileDetails():
    data = request.get_json()
    return profile_updater.getUserCollegeProfile(data["prn_no"],data["clg_id"],mongo)

########### Student Side Exam and Result Quries #############
@app.route('/api/getExams', methods=["POST"])
def getExams():
    # print("getexam")
    data = request.get_json()
    return user_side_queries.getExams(data["clg_id"],data["branch_id"],mongo)

@app.route('/api/getResults', methods=["POST"])
def getResults():
    # print("getResults")
    data = request.get_json()
    return user_side_queries.getResults(data["clg_id"],data["branch_id"],mongo)


####################### College Side Queries #####################

@app.route('/api/collegeGetStudents', methods=["POST"])
def getCollegeStudents():
    # print("getCollegeStudents")
    data = request.get_json()
    return college_side_queries.getStudents(data["clg_id"],mongo)


@app.route('/api/collegeGetExams', methods=["POST"])
def getCollegeExams():
    # print("getCollegeExams")
    data = request.get_json()
    return college_side_queries.getExams(data["clg_id"],mongo)

@app.route('/api/collegeGetResults', methods=["POST"])
def getCollegeResults():
    # print("getCollegeResults")
    data = request.get_json()
    return college_side_queries.getResults(data["clg_id"],mongo)



if __name__ == '__main__':
    app.run(debug=True)