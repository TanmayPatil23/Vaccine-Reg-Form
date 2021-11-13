from datetime import date, datetime
import re

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
      self.validation['email'] = Validation(type = 'string', minLength=5, maxLength=50)
      self.validation['age'] = Validation(type= 'integer', minLength=1, maxLength=3)
      self.validation['gender'] = Validation(type='string', minLength=4, maxLength=6)
      self.validation['city'] = Validation(type='string', minLength = 2, maxLength = 50)
      self.validation['state'] = Validation(type='string', minLength = 2, maxLength = 50)
      self.validation['pin'] = Validation(type='integer', minLength = 6, maxLength = 6)
      self.validation['aadhar'] = Validation(type='integer', minLength = 12, maxLength = 12)
      self.validation['blood_grp'] = Validation(type='string', minLength = 2, maxLength = 3)
      self.validation['dose_num'] = Validation(type='integer', minLength = 1, maxLength = 1)
      self.validation['prev_id'] = Validation(type='integer', minLength = 12, maxLength = 12)
      self.validation['prev_date'] = Validation(type='date', minLength = 10, maxLength = 10)
      self.validation['vaccine_name'] = Validation(type='string', minLength=7, maxLength=10)
      self.validation['preferred_date'] = Validation(type='date', minLength=10, maxLength=10)

      self.testcase = {}
      self.testcase['first_name'] = 'pass'
      self.testcase['middle_name'] = 'pass'
      self.testcase['last_name'] = 'pass'
      self.testcase['dob'] = 'pass'
      self.testcase['mobile'] = 'pass'
      self.testcase['email'] = 'pass'
      self.testcase['age'] = 'pass'
      self.testcase['gender'] = 'pass'
      self.testcase['city'] = 'pass'
      self.testcase['state'] = 'pass'
      self.testcase['pin'] = 'pass'
      self.testcase['aadhar'] = 'pass'
      self.testcase['blood_grp'] = 'pass'
      self.testcase['dose_num'] = 'pass'
      self.testcase['prev_id'] = 'pass'
      self.testcase['prev_date'] = 'pass'
      self.testcase['vaccine_name'] = 'pass'
      self.testcase['preferred_date'] = 'pass'
   
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
         if (field == 'prev_date' or field == 'prev_id') and record['dose_num'] == '1':
            self.testcase[field] = 'pass'
            continue
         if len(data) == 0 or len(data) < minLength or len(data) > maxLength:
            self.testcase[field] = 'fail'
            continue
         elif type == 'date':
            continue
         elif type == 'integer':
            for digit in data:
               if ord(digit) < 48 or ord(digit) > 57:
                  self.testcase[field] = 'fail'
                  break
            continue
         if field == 'email':
            continue
         elif field == 'age':
            continue
         elif field == 'gender':
            if data.lower() not in ['male', 'female', 'other']:
               self.testcase[field] = 'fail'
            continue
         elif field == 'blood_grp':
            data = data.lower()
            if data not in ['a+', 'a-', 'b+', 'b-', 'ab+', 'ab-', 'o+', 'o-']:
               self.testcase[field] = 'fail'
            continue
         elif field == 'dose_num':
            if data not in ['1', '2']:
               self.testcase[field] = 'fail'
            continue
         elif field == 'prev_id':
            if record['dose_num'] == '1':
               self.testcase[field] = 'pass'
               continue
            if self.testcase['aadhar'] == 'fail':
               self.testcase[field] = 'fail'
               continue
            if record['aadhar'] != data:
               self.testcase[field] = 'fail'
            continue
         elif field == 'vaccine_name':
            if data.lower() not in ['covaxin', 'covishield', 'sputnik']:
               self.testcase[field] = 'fail'
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





