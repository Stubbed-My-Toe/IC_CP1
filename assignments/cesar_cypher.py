#IC 1st Cesar cypher
def shift():
    for i in message:
        pos = alphabet.index(i)
    return pos + raw_cipher
#establish alphabet
alphabet = ("abcdefghijklmnopqrstuvwxyz")
#Ask what operation user wants to do
operation =input("What operation do you want to do? Press 1 for encode. Press 2 for decode.\n").strip()
#if statement for 1 and 2
if operation == "1":
    #pick a number for the cesar cypher
    raw_cipher = input("Please pick a number for the cesar cypher\n").strip()
    #check if cypher is valid.
    cipher = raw_cipher.isdigit()
    if cipher:
        print(f"Nice choice!")
        message = input("Now, enter the message you wanted to encode!\n")
        shift()       
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