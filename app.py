from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField

app = Flask(__name__)
app.config['SECRET_KEY'] = '4a7139823b8f9f3f4d5512f7b0b1b9add4cc843c7b4506cba7189305dfe55158'


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name')
    middle_name = StringField('Middle Name')
    last_name = StringField('Last Name')
    dob = StringField('Date of Birth',  render_kw={"placeholder": "dd-mm-yyyy"})
    mobile = StringField('Mobile')
    email = StringField('Email')
    age = StringField('Age')
    gender = StringField('Gender', render_kw={"placeholder": "Male/Female/Other"})
    city = StringField('City')
    state = StringField('State')
    pin = StringField('Zip Code')
    aadhar = StringField('Aadhar Number')
    blood_grp = StringField('Blood Group', render_kw={'placeholder': 'If O positive then write O+'})
    dose_num = StringField('Dose Number', render_kw={"placeholder": "1/2"})
    prev_id = StringField('Prev Dose ID', render_kw={"placeholder": "Required if does number is 2"})
    prev_date = StringField('Prev Dose Date', render_kw={"placeholder": "Required if does number is 2"})
    vaccine_name = StringField('Vaccine Name', render_kw={'placeholder': 'Covaxin/Covishield/Sputnik'})
    preferred_date = StringField('Preffered date of Vaccination', render_kw={"placeholder": "dd-mm-yyyy"})
    submit = SubmitField('Register')
