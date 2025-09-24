# IC 1st Booleans notes

import time
import datetime as date

current_time = time.time()
readable_time = time.ctime(current_time)
new_current_time = date.datetime.now()
hour = new_current_time.strftime("%H")
# minutes = %M
# weekday = %A, %a
# day = %d
# month = %B, %b
# month num = %m
#year = %Y, %y
#seconds = %S
over = True 




print(f"Current time in seconds since January 1, 1970(epoch): {current_time}")
print(f"Current time from: {new_current_time}")
print(f"Today is {readable_time}")
print(f"The hour is: {hour*3}")

print(f"The hour is saved as an integer: {isinstance(hour, int)}")
print(f"The hour is saved as an float: {isinstance(hour, float)}")
print(f"The hour is saved as an strng: {isinstance(hour, str)}")
print(hour.isalpha())

print(f"Hour has a value: {bool(True)}")

#What can a Boolean hold? (i.e. what is a Boolean?)
#What are Booleans normally used for?
#What does bool() let you do?
#What values are considered True? 
#What values are considered False?
#What are some python built-in functions that return a Boolean value?(Try and find 1 more than the example you are given!)
#What are the simple data types?
#What would you use each data type for?
