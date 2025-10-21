#IC 1st Cesar cypher

#establish alphabet
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#Ask what operation user wants to do
operation = input("What operation do you want to do? Press 1 for encode. Press 2 for decode.\n").strip
true_operation = operation.isdigit()
if operation == 1:
    #get cipher
    raw_cipher = input("Please pick a number for the cesar cypher\n").strip()
    cipher = raw_cipher.isdigit()
    if cipher:
        print(f"Nice choice! Shifting cipher by {raw_cipher}.")
        alphabet.rotate(raw_cipher)
        print(alphabet)
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
    print("The input is invalid exiting program now")
    quit()