#IC 1st Idiot Proof

print("What is your first name?")
fname = input().strip().title()

print("What is your last name?")
lname = input().strip().title()

Full_name = fname + " " + lname
print("Name:",Full_name)

print("What is your phone number?")
phone_number = input().strip()
if len(phone_number) == 12:
    return False

return True