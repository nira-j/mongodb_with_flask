from flask_wtf import Form
from wtforms import TextField
from wtforms.fields.simple import SubmitField

class updateform(Form):
    name=TextField("Field name")
    name=TextField("Value")
    submit=SubmitField("Update")
