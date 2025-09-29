#IC 1st lists notes
import random
#every item separated by comma, special brackets, every item must follow data type
sibs = ["Alex", "Katie", "Andrew", "Tia", "Isaac", "Bruce", "Wayne", "Parker", "Jonah", "Brock"]

print(sibs[5])
print(random.choice(sibs, weights=(10,10,10,10,10,10,10,10,10,10), k=5))
print(f"The list is {len(sibs)} people long")
print(sibs)
sibs[0] = "Eric"
sibs[6:-1] = ["Xavier", "Hailey"]
sibs.pop()
sibs.pop(3)
sibs.remove("Isaac")
#sibs.clear() <= commented for safety
#sibs.append("Andrew") <= adds to end of list
sibs.insert(2, "Andrew")
sibs.extend(["Joseph", "Damian", "Crowbar"])
print(sibs)

board = [[1,2,3],
        [4,5,6],
        [7,8,9]
        ]

fruit = ("Apple", "Orange", "Pineapple") #tuple ordered, not changeable

veggies = {"Spinach", "Kale", "Broccoli", "Carrot"} #set unordered unchangeable
