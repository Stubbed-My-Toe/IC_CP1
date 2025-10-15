#IC 1st password strength checker

#Meeting the length requirement: +1 point
#Containing uppercase letters: +1 point
#Containing lowercase letters: +1 point
#Containing numbers: +1 point
#Containing special characters: +1 point

#Length: At least 8 characters long
#Uppercase: Contains at least one uppercase letter
#Lowercase: Contains at least one lowercase letter
#Numbers: Contains at least one number
#Special characters: Contains at least one special character (!@#$%^&*()_+-=[]{}|;:,.<>?)

#1-2 points: Weak. 3 points: Moderate. 4 points: Strong. 5 points: Very Strong.




#show "Hello! This is the Isaac Covington 2100 Password Strength Checker System; or PSCS for short."
print("Hello! This is the Isaac Covington 2100 Password Strength Checker System; or PSCS for short.")
#show "this program checks the strength of your password based on certain criteria, and gives you a score out of 5."
print("This program checks the strength of your password based on certain criteria, and gives you a score out of 5.")

#ask for password, show requirements.
print("Your password must have a length of 8 characters, contain at least one special character, contain at least one capital letter, one lowercase letter, and one number.\nMeeting one requirement gives you one point.")
#have user enter their password
paswrd = input('What is your password?\n').strip()

spec_char = ("!@{#$%^&*()_+-=[]}|;:,.<>?")
numbers = list("1234567890")
points = 0
length = len(paswrd)

if length >= 8:
    points = points + 1
    print("Your password is long enough! +1 point")
else:
    print("your password failed the length test.")


#turn password into list.
characters = list(paswrd)
#loop for i in password
for i in characters:
    special = i in spec_char
    if special:
        points = points + 1
        print("Your password contains a special character! +1 point")
        break
    else:
        continue

for i in characters:
    num = i.isdigit()
    if num:
        points = points + 1
        print("Your password contains a number character! +1 point")
        break
    else:
        continue


for i in characters:
    upperc = i.isupper()
    if upperc:
        points = points +1
        print("Your password contains a capital character! +1 point")
        break
    else:
        continue

for i in characters:
    lowerc = i.islower()
    if lowerc:
        points = points +1
        print("Your password contains a lowercase character! +1 point")
        break
    else:
        continue

#Check each character isupper if at least one is. +1 point
#Check each character islower if at least one is. +1 point
#if len(list) >= 8. +1 point
#Check each character isnumeric if at least one is. +1 point
#check each character if it matches the things on special characters list.


if points < 3:
   print("Your password strength is: weak")
elif points == 3:
   print("Your password strength is: moderate")
elif points == 4:
    print ("Your password strength is: strong")
elif points == 5:
    print("Your password strength is: very strong")
else:
    points == 0
    print ('no points at all? \n Your password strength is: weird')