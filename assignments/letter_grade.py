#IC 1st what is my grade?

#determining grades
grade = float(input("What is your grade?"))
if grade > 100:
 print(f"You have {grade}% which is an A+! I should be taking advice from you!")
elif grade >= 92:
    print(f"You have {grade}% an A! Good job!")
elif grade >= 90 and grade <= 92:
   print(f"You have {grade}% which is an A-. Nice work!")
elif grade >= 87 and grade <= 89:
    print(f"You have {grade}% which is a B+. Not too shabby.")
elif grade >= 82 and grade <= 86:
   print(f"You have {grade}% which is a B. You can do it!")
elif grade >= 80 and grade <=82:
   print(f"You have {grade}% which is a B-. Really?")
elif grade >= 77 and grade<= 79:
   print(f"You have {grade}% which is a C+. Maybe McDonalds is an option?")
elif grade >= 72 and grade <= 76:
   print(f"You have {grade}% which is a C. Stay away from table saws.")
elif grade >= 70 and grade <= 71:
   print(f"You have {grade}% which is a C-. You’re the reason we have warning labels")
elif grade >= 67 and grade <= 69:
   print(f"You have {grade}% which is a D+. I expected nothing, but I'm still disappointed")