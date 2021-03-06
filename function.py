def calculate_age(self, Date):
   split_date = Date.split('-')
   dd, mm, yyyy  = split_date[0], split_date[1], split_date[2]
   today = date.today()
   Date = date(int(yyyy), int(mm), int(dd))
   age = today.year - Date.year - ((today.month, today.day) < (Date.month, Date.day))
   return age


   def validate_date(self, Date):
   format = "%d-%m-%Y"
   try:
      if(bool(datetime.strptime(Date, format))):
         res = 'pass'
   except:
      res = 'fail'
   return res

def validate_gender(self, gender_string):
   gender_string = gender_string.lower()
   if gender_string not in ['male', 'female', 'other']:
      return 'fail'
   return 'pass'


def validate_blood_group(self, blood_group):
   blood_group = blood_group.lower()
   if blood_group not in ['a+', 'a-', 'b+', 'b-', 'ab+', 'ab-', 'o+', 'o-']:
      return 'fail'
   return 'pass'

def validate_str(self, input_string):
   if input_string.isalpha():
      return 'pass'
   else:
      return 'fail'
   
def validate_numeric(self, input_string):
   for character in input_string:
      if character in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
         continue
      else:
         return 'fail'
   return 'pass'

def validate_email(self, email):
   regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
   if(re.fullmatch(regex, email)):
      return 'pass'
   return False
