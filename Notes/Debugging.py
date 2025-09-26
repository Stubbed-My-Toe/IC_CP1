# IC 1st debugging notes

# Syntax error - grammar error
    #print"Vienna"
# => Read error message, go to that line of code, fix the syntax

# Logic errors - we gave the wrong steps
numone = "2"
numtwo = "5"

print(numone + numtwo)

# Have a well thought out 

# Run-time Error
import random
while True:
    denominator = random.randint(1, 5)
    #brute force debugging kinda sucks. see one line below
    print(f"denominator: {denominator}")

    print(10/denominator)
    #read the error that pops up in terminal, fix error
