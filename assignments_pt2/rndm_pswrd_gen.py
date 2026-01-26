#IC CP2 random password generator

#import random
import random

#the lists that will be added to pool
#lower alphabet (abcdefghijk etc.)
#upper alphabet (ABCDEFGHIJK etc.)
#special chars (! @ # $ % ^ & * ( ) _ + - = { } [ ] | \ : ; ' " , . < > ? /)
#numbers (1,2,3,4,5,6,7,8,9,0)

#pool() is where everything goes when the user says they want it, i will be using append, and then one character from pool will be added every time for the length the user decides


#when user enters program, run main menu
#def main menu 
    #Please type number for the input you wouyld like to perform, 1.make password, 2. exit
    #if user says 1, run make_password


#this is for making the passwords
#def make psswrd
    #psswrd length (ask user how long do you want your password to be?)
    #requirements is to make sure what will be added to pool.
    #def requirements
        #Do you want uppercase in your password?Y/N
        #if user responds Y
            #append uppercase to pool
        #elif user = no
            #nothing
        #else:
            #requirements()

        #do you want lowercase in password? y/n
            #if Y
                #append lower alphabet to pool
            #elif N
                #nothing
            #else
                #requirements

        #do you want special in your password? Y/N
            #if Y
                #append special chars to pool
            #elif N
                #nothing
            #else:
                #please try again!
                #requirements()
        
        #do you want numbers in your password? Y/N
            #if Y
                #append numbers to pool
            #elif N
                #nothing
            #else
                #requirements()
#for length in range(psswrd length)
    #password 1 = password1.append(random.choice(pool))
#for length in range(psswrd length)
    #password 2 = password1.append(random.choice(pool))
#for length in range(psswrd length)
    #password 3 = password1.append(random.choice(pool))
#for length in range(psswrd length)
    #password 4 = password1.append(random.choice(pool))

#possible passwords
#print(password 1\n, password 2\n, password 3\n, password 4\n)
#main menu()