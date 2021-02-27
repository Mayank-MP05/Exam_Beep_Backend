import json
def getExams(clg_id,branch_id,mongo):
    # print(clg_id, branch_id, mongo)
    getter = mongo.db.exams.find({
        "branch_id": branch_id,
        "clg_id":clg_id
    })
    elist = []
    for doc in getter:
        elist.append(doc)
    return json.dumps({"exams":elist},default=str)

def getResults(clg_id,branch_id,mongo):
    # print(clg_id, branch_id, mongo)
    getter = mongo.db.results.find({
        "branch_id": branch_id,
        "clg_id":clg_id
    })
    elist = []
    for doc in getter:
        elist.append(doc)
    return json.dumps({"results":elist},default=str)