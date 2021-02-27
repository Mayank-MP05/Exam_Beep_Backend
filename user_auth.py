from flask import jsonify
import json
import random

# Login Function


def login(email,password, mongo):
    getter = mongo.db.users.find_one({"email": email})
    # if user is not present in DB
    if getter is None:
        print("nothing found in user")
        return jsonify({
            "err": f'No user exists with email {email}'
        })
    else:
        if getter["password"] == password:
            print("GO GO GO")
            print(getter)
            # getter._id = None
            # getter.password = None
            return json.dumps(getter, default=str)
        else:
            return jsonify({
                "err": f'Wrong Password'
            })

# Signup Function


def signup(email,name, pass1, pass2, mongo):
    dp = random.randint(0, 8)
    if pass1 != pass2:
        return jsonify({
            "err": "Password do not match!",
        })
    getter = mongo.db.users.insert_one({
        "name": name,
        "password": pass1,
        "prn_no": "",
        "clg_id": "",
        "email": email,
        "profilePic": dp,
        # "isCollege": isCollege
    }).inserted_id
    # if user is not present
    if getter is None:
        return jsonify({
            "err": "Something error occurred!"
        })
    else:
        setter = mongo.db.users.find_one({"_id": getter})
        return json.dumps(setter, default=str)
