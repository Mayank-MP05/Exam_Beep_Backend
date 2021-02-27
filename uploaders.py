import io
import csv
from flask import jsonify

def upload(file,data,mongo):
    if not file:
        return jsonify({
            "status":"No file"
        })
        
    stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
    csv_input = csv.reader(stream)
    #print("file contents: ", file_contents)
    #print(type(file_contents))
    # print(csv_input)
    for row in csv_input:
        # print(row)
        if data == "students":
            students = [ "clg_id", "prn_no","name","branch_id","age"]
            doc={}
            # can be optimized by iterating over the set instead of array
            for n in range(0,len(students)):
                doc[students[n]] = row[n]

            mongo.db.students.insert_one(doc)
        elif data == "exams":
            exams = [ "clg_id", "branch_id","subject","deadline_of_reg","restration_link","exam_date","exam_link"]
            doc={}
            for n in range(0,len(exams)):
                doc[exams[n]] = row[n]

            mongo.db.exams.insert_one(doc)
        else:
            results = [ "clg_id", "branch_id","date_of_declaration","result_link"]
            doc={}
            for n in range(0,len(results)):
                doc[results[n]] = row[n]

            mongo.db.results.insert_one(doc)
    return jsonify({
        "status":"200",
        "Coll":data
    })

