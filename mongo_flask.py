from pymongo import MongoClient
from pprint import pprint
from flask import Flask, render_template
from flask import request
app=Flask(__name__)

client=MongoClient("")
db=client.persons


app.run(debug=True)
