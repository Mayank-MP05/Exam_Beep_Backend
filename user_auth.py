from flask import jsonify
import json
import random

#Login Function
def login(email,password,isCollege,mongo):
    getter = mongo.db.users.find_one({"email":email})
    #if user is not present in DB
    if getter is None:
        print("No user exists with this Email id")
    else:
        print("Good Going !!!")

def signup(email,pass1,pass2,isCollege,mongo):
    if pass1 != pass2:
        print("password do not match bruh")
    else:
        print("working")