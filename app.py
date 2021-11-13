from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from testing_tool import Validation_Tool

app = Flask(__name__)
app.config['SECRET_KEY'] = '4a7139823b8f9f3f4d5512f7b0b1b9add4cc843c7b4506cba7189305dfe55158'
class RegistrationForm(FlaskForm):
    first_name = StringField('First Name')
    middle_name = StringField('Middle Name')
    last_name = StringField('Last Name')
    # -, /, .
    dob = StringField('Date of Birth',  render_kw={"placeholder": "dd-mm-yyyy"})
    mobile = StringField('Mobile')
    email = StringField('Email')
    age = StringField('Age')
    gender = StringField('Gender', render_kw={"placeholder": "Male/Female/Other"})
    city = StringField('City')
    state = StringField('State')
    pin = StringField('Zip Code')
    aadhar = StringField('Aadhar Number')
    blood_grp = StringField('Blood Group', render_kw={
                            'placeholder': 'If O positive then write O+'})
    dose_num = StringField('Dose Number', render_kw={
                           "placeholder": "1/2"})
    prev_id = StringField('Prev Dose ID', render_kw={
                          "placeholder": "Required if dose number is 2"})
    prev_date = StringField('Prev Dose Date', render_kw={
                            "placeholder": "Required if does number is 2"})
    vaccine_name = StringField('Vaccine Name', render_kw={
        'placeholder': 'Covaxin/Covishield/Sputnik'})
    preferred_date = StringField('Preffered date of Vaccination', render_kw={
                                 "placeholder": "dd-mm-yyyy"})
    submit = SubmitField('Register')

class ValidateForm(FlaskForm):
    submit = SubmitField('Validate Form')

@app.route('/')
@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        record = dict()
        record['first_name'] = form.first_name.data 
        record['middle_name'] = form.middle_name.data
        record['last_name'] = form.last_name.data
        record['dob'] = form.dob.data
        record['mobile'] = form.mobile.data
        record['email'] = form.email.data
        record['age'] = form.age.data
        record['gender'] = form.gender.data
        record['city'] = form.city.data
        record['state'] = form.state.data
        record['pin'] = form.pin.data
        record['aadhar'] = form.aadhar.data
        record['blood_grp'] = form.blood_grp.data
        record['dose_num'] = form.dose_num.data
        record['prev_id'] = form.prev_id.data
        record['prev_date'] = form.prev_date.data
        record['vaccine_name'] = form.vaccine_name.data
        record['preferred_date'] = form.preferred_date.data
        file = open('records.txt', 'a')
        file.write(str(record))
        file.write('\n')
        file.close()
        return redirect('validate')
    else:
        return render_template('register.html', title='Registration From', form=form)
    return render_template('register.html', title='Registration From', form=form)

@app.route('/validate', methods=['GET', 'POST'])
def validate():
    form = ValidateForm()
    if request.method == 'POST' and form.validate_on_submit():
        file = open('records.txt')
        record = file.read()
        file.close()
        tool = Validation_Tool()
        record = tool.validate(record.splitlines()[-1])
        return render_template('validate.html', title='Validate', record=record, testcase=tool.testcase)
    else:
        return render_template('validate.html', title='Validate', form = form, result='none')

if __name__ == '__main__':
    app.run(debug=True)