import json

def updateProfile(email,prn_no,clg_id,mongo):
    # print(email, prn_no, clg_id, mongo)
    getter = mongo.db.users.find_one({
        "email": email,
    })
    mongo.db.users.update_one({
    '_id': getter["_id"]
    },{
    '$set': {
        'prn_no':prn_no,
        'clg_id':clg_id,
    }
    }, upsert=False)
    getter = mongo.db.users.find_one({
        "email": email,
    })
    return json.dumps(getter,default=str)

def getProfileFromStuds(email,mongo):

    # print(prn_no, clg_id, mongo)
    getter = mongo.db.users.find_one({
        "email":email
    })
    return json.dumps(getter,default=str)


def getUserCollegeProfile(prn_no,clg_id,mongo):
    getter = mongo.db.students.find_one({
        "clg_id":clg_id,
        "prn_no":prn_no
    })
    return json.dumps(getter,default=str)
