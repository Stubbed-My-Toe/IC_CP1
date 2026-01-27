#IC CP2 random password generator

#import random
import random

#the lists that will be added to pool
#lower alphabet (abcdefghijk etc.)
lower_alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#upper alphabet (ABCDEFGHIJK etc.)
upper_alphabet =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#special chars (! @ # $ % ^ & * ( ) _ + - = { } [ ] | \ : ; ' " , . < > ? /)
special_chars = ["!","@","#","$","%","^","&","*","(",")","_","+","-","=","{","}","[","]","|", ":", ";", ",", ".", "<", ">", "?", "/"]
#numbers (1,2,3,4,5,6,7,8,9,0)
numbers =["1","2","3","4","5","6","7","8","9","0"]

password_1 = []
password_2 = []
password_3 = []
password_4 = []
#pool() is where everything goes when the user says they want it, i will be using append, and then one character from pool will be added every time for the length the user decides
pool = []

#when user enters program, run main menu
#def main menu
def main():
    #Please type number for the input you wouyld like to perform, 1.make password, 2. exit
    main_choice = input("Please type the number of the input you want to perform. \n1. Make random password\n2. Exit program\n")
    #this is for making the passwords
    #def make psswrd
    def make_paswrd():
        #psswrd length (ask user how long do you want your password to be?)
        paswrd_length = int(input("How long do you want your password to be? "))
        #requirements is to make sure what will be added to pool.
        #def requirements
        def requirements():
            #Do you want uppercase in your password?Y/N
            uppercase_YN = input("Do you want uppercase letters in your password? Y/N: ")
            #if user responds Y
            if uppercase_YN == "Y":
                #append uppercase to pool
                pool.append(upper_alphabet)
            #elif user = no
            elif uppercase_YN == "N":
                #nothing
                print("")
            #else:
            else:
                #requirements()
                requirements()

            #do you want lowercase in password? y/n
            lowercase_YN = input("Do you want lowercase letters in your password? Y/N: ")
            #if user = Y
            if lowercase_YN == "Y":
                #append lower alphabet to pool
                pool.extend(lower_alphabet)
            #elif N
            elif lowercase_YN == "N":
                #nothing
                print("")
            #else
            else:
                #requirements
                requirements()

            #do you want special in your password? Y/N
            special_YN = input("Do you want special characters in your password? Y/N: ")
            #if Y
            if special_YN == "Y":
                #append special chars to pool
                pool.extend(special_chars)
            #elif N
            elif special_YN == "N":
                print("")
                #nothing
            #else:
            else:
                requirements()
                #please try again!
                #requirements()
            
            #do you want numbers in your password? Y/N
            numbers_YN = input("Do you want numbers in your password? Y/N: ")
                #if Y
            if numbers_YN == "Y":
                #append numbers to pool
                pool.extend(numbers)
            #elif N
            elif numbers_YN == "N":
                print()
                #nothing
            #else
            else:
                requirements()
                #requirements()
        requirements()

    #for length in range(psswrd length)
        #password 1 = password1.append(random.choice(pool))
        password_1.append(random.sample(pool, paswrd_length))
        #for length in range(psswrd length)
        #password_2 = password_2.append(random.choice(pool))
        password_2.append(random.sample(pool, paswrd_length))
        #for length in range(psswrd length)
        #password 3 = password1.append(random.choice(pool))
        password_3.append(random.sample(pool,paswrd_length))
        #for length in range(psswrd length)
        #password 4 = password1.append(random.choice(pool))
        password_4.append(random.sample(pool, paswrd_length))
        #print(password 1\n, password 2\n, password 3\n, password 4\n)    
        print(f"\nHere are your passwords: {password_1}\n {password_2}\n {password_3}\n {password_4}\n")
        main()

    if main_choice =="1": 
        make_paswrd()
    #if user says 1, run make_password
    elif main_choice == "2":
        exit()
    else:
        print("Please try again")
        main()


main()


#I couldn't figure out how to not make the passwords so weirdly formatted. Sorry.