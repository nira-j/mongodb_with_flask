from flask import Flask, request,redirect, url_for, render_template, jsonify
from pymongo import MongoClient

app=Flask(__name__)
client=MongoClient("mongodb://127.0.0.1:27017")
db = client.students
collection = db.xavier

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/insertrecord", methods=["POST","GET"])
def insertrecord():
    if request.method=="POST":
        stu_name=request.form.get("stu_name")
        stu_class=request.form.get("stu_class")
        stu_roll=request.form.get("stu_roll")
        stu_gen=request.form.get("stu_gen")
        stu_col=request.form.get("stu_col")
        stu_con=request.form.get("stu_con")
        data={
            "student name": stu_name,
            "student class": stu_class,
            "student roll no": stu_roll,
            "student gender": stu_gen,
            "student college": stu_col,
            "student contact": stu_con
        }
        if (stu_name !="" and stu_class !="" and stu_roll !="" and stu_gen !="" and stu_col !="" and stu_con !="" ):
            out=collection.insert_one(data)
            if out:
                return render_template("success.html")
        else:
            return render_template("insert.html")

    return render_template("insert.html")
@app.route('/deleterecord/<string:obj_id>')
def deleterecord(obj_id):
    collection.delete_one({'student name': obj_id})
    return redirect(url_for("showrecord"))
    
@app.route('/updaterecord',methods=["POST","GET"])
def updaterecord():
    return render_template('update.html')

@app.route("/showrecord", methods=["GET"])
def showrecord():
    output=collection.find()
    out=[]
    for o in output:
        out.append(o)
    return render_template("show.html",output=out)

app.run(debug=True, host="10.160.0.6")