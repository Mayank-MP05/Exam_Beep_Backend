import json
def getExams(clg_id,branch_id,mongo):
    # print(clg_id, branch_id, mongo)
    getter = mongo.db.exams.find({
        "branch_id": branch_id,
        "clg_id":clg_id
    })
    lst = []
    for doc in getter:
        lst.append(doc)
    return json.dumps({"exams":lst},default=str)

def getResults(clg_id,branch_id,mongo):
    # print(clg_id, branch_id, mongo)
    getter = mongo.db.results.find({
        "branch_id": branch_id,
        "clg_id":clg_id
    })
    lst = []
    for doc in getter:
        lst.append(doc)
    return json.dumps({"results":lst},default=str)