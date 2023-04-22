import datetime
#This command imports datetime into our script

time_now = datetime.datetime.now()

time_now_str = time_now.strftime("%I:%M:%S %p")
# I use strftime to properly convert the time to a string ,
# in which time_now is the result. Strftime is also used to 
# display the time in a normal format not miliary time.

print("Right now the time is:", time_now_str)



