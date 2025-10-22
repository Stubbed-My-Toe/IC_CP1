#IC 1st Cesar cypher

#pick a number for the cesar cypher
#establish alphabet
alphabet = ("abcdefghijklmnopqrstuvwxyz")
#Ask what operation user wants to do
operation =input("What operation do you want to do? Press 1 to encode. Press 2 to decode.\n").strip()
raw_cipher = int(input("Please pick a number for the cesar cypher. A is at 0, B is at 1, C is at 2, and so on\n").strip())
def shift():
    if raw_cipher >= 26:
        raw_cipher % 26
#if statement for 1 and 2
if operation == "1":
    #check if cypher is valid.
    cipher = raw_cipher
    if cipher:
        print(f"Nice choice!")
        message = input("Now, enter the message you wanted to encode!\n")
        shift()       
        print()
    else:
        print("The number you entered is not valid. Exiting program now...")
        quit()
#operation 2
elif operation == 2:
    raw_cipher = input("Please pick the number to solve the cesar cipher.\n").strip()
    cipher = raw_cipher.isdigit()
    if cipher:
        print(f"Alright, shifting by {raw_cipher} now.")
else:
    print("The input is invalid, exiting program now")
    quit()