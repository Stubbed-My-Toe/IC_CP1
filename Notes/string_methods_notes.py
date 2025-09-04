#IC String Methods Notes

#subject = "Computer programming 1"
#print(subject.upper())

#print(subject.center(100))

#stupid/idiot proofing inputs
#color = input("What is your favorite color?").strip().capitalize()
#Lower() => all lower case
#upper() => all upper case
#capitalize() => first letter of first word
#title() => capitalize first letter of each word
#full_name = input("What is your full name?").strip().title()
#print("That is cool " + full_name + ". I like " + color + " too!")
#print("That is cool {full_name}. I like {color} too!".format(full_name=full_name,color=color))

#f-strings
#print(f"That is cool {full_name}. I like {color} too!")

pi = "3.14159"
#print(f"We all know pi is equal to {pi:.3f}")
#print(f"We all know piis equal to {pi:.3f})
#print(pi.isdecimal())

sentence = "The quick brown fox jumps over the laxy dog."
word = "jumps"
print(sentence.find(word))
start = sentence.index(word)
length = len(word)
print(sentence[start:start+length])
print(sentence.replace(word, "swims"))
print(sentence)