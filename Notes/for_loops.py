# IC 1st for loops notes!

import time

nums = [54,33,43,543,2,658,776,1,4356,7,6,21,56,]

#for Num(current item) IN Nums(list)
for num in nums:
    num /= 2
    if num > 100:
        print(f"{num} is only half of {num*2}. It is a large number.")
    else:
        print(num)

print("The loop is over")

health = 15

for num in range(1,health,2):
    print(num)
    time.sleep(2)

for num in range(20,0,-2):
    print(num)