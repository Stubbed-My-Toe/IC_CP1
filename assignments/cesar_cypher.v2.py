#IC 1st Caesar Cypher
import string
#estalish alphabet
string.ascii_lowercase
string.ascii_uppercase

#ask for operation.
operation = input("What operation do you want to do? Press 1 to encode. Press 2 to decode.\n").strip()

if operation == "1":
    #estalish alphabet
    alphabet = ("abcdefghijklmnopqrstuvwxyz")
    #Ask for cipher key and text
    text = str(input("What is the message you want to encode?\n")).strip().lower()
    key = int(input("What is the key to the cipher?\n"))
    if 0 < key <= 26:
        for i in text:
elif operation == 2:
    back_alphabet = "zyxwvutsrqponmlkjihgfedcba"
else:
    print("You need to enter a number between 1 and 26.")
