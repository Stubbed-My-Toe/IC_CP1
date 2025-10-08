#Ic 1st while loops notes

#for loop

#These do the same thing
#num = 1 # iterator
#while num <= 20:#<-----End break condition
   # print(num)
    #num += 1 # Increase iterator


#These do the same thing
#for num in range(1,21):
 #   print(num)#what loop does

import time
import random
#infinite loop
num = 1

while num <= 20:
    time.sleep(.001)
    print(1) 
    num+=1 #Prevents infinite loop

goose = random.randint(1,20)
count = 1
while count != goose:
    count += 1
    print("duck")
    if count == 6:
        break
else:
    print("GOOSE!!")

print("The code is done")




i = 0

while i<20:
    i+=1
    if i == 10:
        print("i is 10")
        continue
    else:
        print(f"{i} iteration of the loop")
   

print("The loop ended!")
