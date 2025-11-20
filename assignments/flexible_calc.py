#IC 1st flexible calculator

import math

#Print(welcome message)
print("Welcome to the flexible calculator!")

#available operations= sum, which is x+b. average, which is x+b divided by how many characters. max, which is the highest number. min, which is the lowest. Product which is x*b.
operation=input("What operation do you want to perform? Sum, Average, Max, Min, or Product?\n")
#ask which one.\n



#def sum(x,b)
def sum_op(*num_list,tot_sum,num):
#nums = enter numbers
    num_list = print("Enter numbers\n (type 'done' when finished):")
    if num_list == float() or int():
        print(f"Number:{num_list}")
    elif num_list == "done":
        for num in num_list:
            #1+2+3+4+5 etc
            tot_sum += num
            print(tot_sum)
            return
    else:
        print("Please try again.")
        return
    


#def average()
def average_op(*num_list,tot_sum,num):
    num_list = print("Enter numbers\n (type 'done' when finished):")
    if num_list == float() or int():
        print(f"Number:{num_list}")
    elif num_list == "done":
        for num in num_list:
            #1+2+3+4+5 etc
            #for num in nums, add number and divide by how many numbers there are
            #(1+2+3)/3
            tot_sum = ((tot_sum + num)/num_list.len())
            print(tot_sum)
            return
    else:
        print("Please try again.")
        return

    
#def max()
def max_op(*num_list,max_num):
    num_list = print("Enter numbers\n (type 'done' when finished):")
    if num_list == float() or int():
        print(f"Number:{num_list}")
    elif num_list == "done":
        max_num = max(num_list)
        print(max_num)
        return
    else:
        print("Please try again.")
        return
#what is the highest number in the list?
#organize them by value and pick the index with the highest number

#defmin()
def min_op(*num_list,min_num):
#same asmax, but the smallest number instead
    num_list = print("Enter numbers\n (type 'done' when finished):")
    if num_list == float() or int():
        print(f"Number:{num_list}")
    elif num_list == "done":
        min_num = min(num_list)
        print(min_num)
        return
    else:
        print("Please try again.")
        return

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