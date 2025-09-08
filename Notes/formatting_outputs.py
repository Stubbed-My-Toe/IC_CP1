#IC 1st period Formatting Outputs notes

#How do I write the format method
name = "Jake"
age = 12
money = 21903954365
percent = .74

print("Hello {}, you are {:b}. That is so old! You have ${:.2f} you must be rich! Random percent is {:%}.".format(name, age, money, percent))


print(f"Hello {name}, you are {age:,}. That is so old! You have ${money:.2f} you must be rich! Random percent is {88/100:%}.")
