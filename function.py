   def calculate_age(self, dob_string):
      dob_parts = dob_string.split('-')
      dd, mm, yyyy  = dob_parts[0], dob_parts[1], dob_parts[2]
      today_date = date.today()
      dob_date = date(int(yyyy), int(mm), int(dd))
      age = today_date.year - dob_date.year - ((today_date.month, today_date.day) < (dob_date.month, dob_date.day))
      print("Age=", age)
      return age



   def validate_date(self, date_string):
      date_format = "%d-%m-%Y"
      try:
         if(datetime.strptime(date_string, date_format)):
            res = 'pass'
      except:
         res = 'fail'
      return res

   def validate_blood_group(self, blood_group):
      blood_group = blood_group.lower()
      if blood_group not in ['a+', 'a-', 'b+', 'b-', 'ab+', 'ab-', 'o+', 'o-']:
         return 'fail'
      return 'pass'

   



def validate_str(string: str):
  return 'pass' if string.isalpha() else 'fail'
