from datetime import date, datetime
import re

class Testcase():
   def __init__(self, result = 'pass', msg = ''):
      self.result = result
      self.msg = msg

class Validation():
   def __init__(self, type, minLength, maxLength):
      self.type = type
      self.minLength = minLength
      self.maxLength = maxLength

class Validation_Tool():
   def __init__(self):
      self.validation = {}
      self.validation['first_name'] = Validation(type = 'string', minLength = 2, maxLength = 50)
      self.validation['middle_name'] = Validation(type = 'string', minLength = 2, maxLength = 50)
      self.validation['last_name'] = Validation(type = 'string', minLength = 2, maxLength = 50)
      self.validation['dob'] = Validation(type = 'date', minLength = 10, maxLength=10)
      self.validation['mobile'] = Validation(type = 'integer', minLength=10, maxLength =10)
      self.validation['email'] = Validation(type = 'email', minLength=5, maxLength=50)
      self.validation['age'] = Validation(type= 'integer', minLength=1, maxLength=3)
      self.validation['gender'] = Validation(type='string', minLength=4, maxLength=6)
      self.validation['city'] = Validation(type='string', minLength = 2, maxLength = 50)
      self.validation['state'] = Validation(type='string', minLength = 2, maxLength = 50)
      self.validation['pin'] = Validation(type='integer', minLength = 6, maxLength = 6)
      self.validation['aadhar'] = Validation(type='integer', minLength = 12, maxLength = 12)
      self.validation['blood_grp'] = Validation(type='blood_grp', minLength = 2, maxLength = 3)
      self.validation['dose_num'] = Validation(type='integer', minLength = 1, maxLength = 1)
      self.validation['prev_id'] = Validation(type='integer', minLength = 0, maxLength = 12)
      self.validation['prev_date'] = Validation(type='date', minLength = 0, maxLength = 10)
      self.validation['vaccine_name'] = Validation(type='string', minLength=7, maxLength=10)
      self.validation['preferred_date'] = Validation(type='date', minLength=10, maxLength=10)

      self.testcase = {}
      self.testcase['first_name'] = Testcase()
      self.testcase['middle_name'] = Testcase()
      self.testcase['last_name'] = Testcase()
      self.testcase['dob'] = Testcase()
      self.testcase['mobile'] = Testcase()
      self.testcase['email'] = Testcase()
      self.testcase['age'] = Testcase()
      self.testcase['gender'] = Testcase()
      self.testcase['city'] = Testcase()
      self.testcase['state'] = Testcase()
      self.testcase['pin'] = Testcase()
      self.testcase['aadhar'] = Testcase()
      self.testcase['blood_grp'] = Testcase()
      self.testcase['dose_num'] = Testcase()
      self.testcase['prev_id'] = Testcase()
      self.testcase['prev_date'] = Testcase()
      self.testcase['vaccine_name'] = Testcase()
      self.testcase['preferred_date'] = Testcase()

   def validate_date(self, Date):
      format = "%d-%m-%Y"
      try:
         if(bool(datetime.strptime(Date, format))):
            res = 'pass'
      except:
         res = 'fail'
      return res

   def calculate_age(self, Date):
      # print(Date)
      split_date = Date.split('-')
      dd, mm, yyyy  = split_date[0], split_date[1], split_date[2]
      today = date.today()
      Date = date(int(yyyy), int(mm), int(dd))
      age = today.year - Date.year - ((today.month, today.day) < (Date.month, Date.day))
      # print(age)
      return age
   
   def validate_email(self, email):
      regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
      if(re.fullmatch(regex, email)):
         return 'pass'
      return False
   
   def validate_gender(self, gender):
      gender = gender.lower()
      if gender not in ['male', 'female', 'other']:
         return 'fail'
      return 'pass'

   def validate_blood_group(self, blood_group):
      blood_group = blood_group.lower()
      if blood_group not in ['a+', 'a-', 'b+', 'b-', 'ab+', 'ab-', 'o+', 'o-']:
         return 'fail'
      return 'pass'

   def validate_str(self, input_string):
      # if input_string.isalpha():
      #    return 'pass'
      # else:
      #    return 'fail'
      for i in input_string:
         if i.isalpha() or i.isspace(): continue
         else: return 'fail'
      return 'pass'

   def validate_numeric(self, input_string):
      for character in input_string:
         if character not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return 'fail'
      return 'pass'
   
   def validate(self, record):
      record = record.strip().rstrip('\n')[1:-1]
      pairs = record.split(',')
      record = {}
      for pair in pairs:
         split_pair = pair.strip().split(':')
         key, value = split_pair[0].strip().replace("'", ''), split_pair[1].strip().replace("'", '')
         record[key] = value
      for field in record:
         data = record[field].strip()
         type = self.validation[field].type
         minLength = self.validation[field].minLength
         maxLength = self.validation[field].maxLength
         if len(data) < minLength or len(data) > maxLength:
            self.testcase[field].result = 'fail'
            self.testcase[field].msg = f'LengthError: possible minLength: {minLength} & maxLength: {maxLength}'
            continue
         elif type == 'date':
            self.testcase[field].result = self.validate_date(data)
            if self.testcase[field].result == 'fail':
               self.testcase[field].msg = 'DateError: Invalid Date format'
            if self.testcase[field].result == 'pass' and (field == 'dob' or field == 'prev_date'):
               # Date must be less than current date
               if(self.calculate_age(data) <= 0):
                  self.testcase[field].result = 'fail'
                  self.testcase[field].msg = 'DateError: Date must be less than current date'
                  continue
                  # Date must be greater than current date
            elif self.testcase[field].result == 'pass' and field == 'preferred_date':
               if(self.calculate_age(data) > 0):
                  self.testcase[field].result = 'fail'
                  self.testcase[field].msg = 'DateError: Date must be greater than current date'
                  continue
         elif type == 'string':
            self.testcase[field].result = self.validate_str(data)
            if self.testcase[field].result == 'fail':
               self.testcase[field].msg = 'StringError: Only alphabetical character allowed'
               continue
         elif type == 'integer':
            self.testcase[field].result = self.validate_numeric(data)
            if self.testcase[field].result == 'fail':
               self.testcase[field].msg = 'IntegerError: Only integer allowed'
               continue
         if field == 'email':
            self.testcase[field].result = self.validate_email(data)
            if self.testcase[field].result == 'fail':
               self.testcase[field].msg = 'EmailError: Invalid email id'
               continue
         elif field == 'age':
            if self.testcase['dob'].result == 'fail':
               self.testcase[field].result = 'fail'
               self.testcase[field].msg = 'AgeError: DOB is Invalid hence Age is Invalid'
               continue
            age = self.calculate_age(record['dob'])
            if int(data) != age:
               self.testcase[field].result = 'fail'
               self.testcase[field].msg = f'AgeError: Age must be {age} from according to {record["dob"]}'
            continue
         elif field == 'gender':
            self.testcase[field].result = self.validate_gender(data)
            if self.testcase[field].result == 'fail':
               self.testcase[field].msg = 'GenderError: Invalid gender. Valid gender are "male", "female", "other"'
               continue
         elif field == 'blood_grp':
            self.testcase[field].result = self.validate_blood_group(data)
            if self.testcase[field].result == 'fail':
               self.testcase[field].msg = "BloodGroupError: Invalid data. Valid blood groups are 'a+', 'a-', 'b+', 'b-', 'ab+', 'ab-', 'o+', 'o-'"
               continue
         elif field == 'dose_num':
            if data not in ['1', '2']:
               self.testcase[field].result = 'fail'
               self.testcase[field].msg = 'DoseNumError: Invalid dose num. Possible dose num are 1 and 2'
            continue
         elif field == 'prev_id':
            if record['dose_num'] == '1':
               if len(data) != 0:
                  self.testcase[field].result = 'fail'
                  self.testcase[field].msg = 'PrevIdError: PrevID must be empty as current dose num is 1'
                  continue
               else:
                  self.testcase[field].result = 'pass'
                  continue
            if self.testcase['aadhar'].result == 'fail':
               self.testcase[field].result = 'fail'
               self.testcase[field].msg = 'PrevIdError: Aadhar field is invalid. So does prevID'
               continue
            if record['aadhar'] != data:
               self.testcase[field].result = 'fail'
               self.testcase[field].msg = f'PrevIdError: prev id must be equal to {record["aadhar"]}'
            continue
         elif field == 'prev_date':
            if record['dose_num'] == '1':
               if len(data) == 0:
                  self.testcase[field].result = 'pass'
               else:
                  self.testcase[field].result = 'fail'
                  self.testcase[field].msg = 'DateError: prev date must be empty as dose num is 1'
         elif field == 'vaccine_name':
            if data.lower() not in ['covaxin', 'covishield', 'sputnik']:
               self.testcase[field].result = 'fail'
               self.testcase[field].msg = "VaccineNameError: Invalid Vaccine name. Valid vaccine names are 'covaxin', 'covishield', 'sputnik'"
            continue
      return record
         
if __name__ == '__main__':
   tool = Validation_Tool()
   file = open('records.txt')
   record = file.read()
   file.close()
   record = tool.validate(record.splitlines()[-1])
   print(record)
   print(tool.testcase)





