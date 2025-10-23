#IC 1st Caesar Cypher

#ask for operation.
operation = input("What operation do you want to do? Press 1 to encode. Press 2 to decode.\n").strip()

#ask for text and key
text = str(input("What is the text you want to use?\n")).strip().lower()
key = int(input("What is the key to the cipher?\n"))
#figure out end index

def shift(selected_letters):
    selected_letters = alphabet[0:key]
    
def cipher():
#estalish alphabets
if operation == "1":
    alphabet = "abcdefghijklmnopqrstuvwxyz"
elif operation == 2:
    back_alphabet = "zyxwvutsrqponmlkjihgfedcba"
else:
    print("You need to enter either 1 or 2")
    