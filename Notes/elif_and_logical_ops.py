#IC 1st elif and logical ops

grade = 100

if grade > 100:
    print(f"You did extra credit. . . you did {grade - 100}% extra credit!")
elif grade == 100:
    print("Your grade is perfect!")
else:
    print(f"Try harder you only have {grade}.")

username = "Isaac"
password = "batman"

user = input("Enter your username: ")
pword = input("enter your passsword")

if not user or not pword:
    print("Please actually write something")
elif user == "Tia" and pword == "password":
    if pword =="password":
        print("welcome Tia")
    else:
        print("Password incorrect")
elif user == username and pword == password:
    print("Welcome Isaac")
elif user == username:
    print("password incorrect")
else:
    print("Incorrect credentials")