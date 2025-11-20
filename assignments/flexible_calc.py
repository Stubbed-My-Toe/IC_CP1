#IC 1st flexible calculator

import math

#Print(welcome message)
print("Welcome to the flexible calculator!")

#available operations= sum, which is x+b. average, which is x+b divided by how many characters. max, which is the highest number. min, which is the lowest. Product which is x*b.
operation=input("What operation do you want to perform? Sum, Average, Max, Min, or Product?\n")
#ask which one.\n



#def sum(x,b)
def sum(*num_list,):
#nums = enter numbers
    num_list = print("Enter numbers\n (type 'done' when finished):")
    if num_list == float() or int():
        print(f"Number:{num_list}")
    elif num_list == "done":
        for num in num_list:
            #1+2+3+4+5 etc
            tot_sum += num
    else:
        print("Please try again.")
        return
    


#def average()
def average(*num_list):
    num_list = print("Enter numbers\n (type 'done' when finished):")
    if num_list == float() or int():
        print(f"Number:{num_list}")
    elif num_list == "done":
        for num in num_list:
            #1+2+3+4+5 etc
            #for num in nums, add number and divide by how many numbers there are
            #(1+2+3)/3
            tot_sum = ((tot_sum + num)/num_list.len())
    else:
        print("Please try again.")
        return

    
#def max()
def max():
    
#what is the highest number in the list?
#organize them by value and pick the index with the highest number

#defmin()
#same asmax, but the smallest number instead

#defproduct()
#product_answ = x*b*c


#while loop

#have them keep putting num in until
#stop when input = done


#call func and do calculation
#ask do you want to go again?
yeon = input("Do you want to do another operation? y/n\n")
if yeon == "y":
    an_operation=input("What operation do you want to perform? Sum, Average, Max, Min, or Product?\n")


#if input = yes keep going
#reset nums
#else= print thank you for using the calcuator! break
elif yeon == "n":
    print("Thank you for using the calculator.")
    quit()