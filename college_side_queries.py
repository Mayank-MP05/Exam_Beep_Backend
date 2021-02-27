import json
def getStudents(clg_id,mongo):
    # print(clg_id, mongo)
    getter = mongo.db.students.find({
        "clg_id":clg_id
    })
    lst = []
    for doc in getter:
        lst.append(doc)
    return json.dumps({"data":lst},default=str)

def getExams(clg_id,mongo):
    # print(clg_id, mongo)
    getter = mongo.db.exams.find({
        "clg_id":clg_id
    })
    lst = []
    for doc in getter:
        lst.append(doc)
    return json.dumps({"data":lst},default=str)

def getResults(clg_id,mongo):
    # print(clg_id, mongo)
    getter = mongo.db.results.find({
        "clg_id":clg_id
    })
    lst = []
    for doc in getter:
        lst.append(doc)
    return json.dumps({"data":lst},default=str)