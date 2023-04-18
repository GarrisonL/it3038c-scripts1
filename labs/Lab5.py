import datetime


birthdate_str = input("Input your birthdate with 'YYYY-MM-DD': ")
#This will be asking the user to enter their bday

birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")
#turns the birthdate string into an object using datetime

age_in_seconds = (datetime.datetime.now() - birthdate).total_seconds()
#this performs the math for age to seconds

print("In counting you are" , age_in_seconds, "seconds old")
