#IC 1st Combat Activity Diagram

import random
print("Welcome to the combat program.\nI ask that you give me your name and specialties before we start.")
name = input("What is your name?\n")
grade = int(input("Press 1 if you are a fighter, 2 if you are a mage, and 3 if you are a rogue.\n"))
diff = int(input("What is your desired difficulty of combat? Press 1 for easy, 2 for medium, and 3 for hard.\n(dev note: Have not fully worked out difficulties for now, just pick one, they are all the same)\n"))

fhealth = 25 + random.randint(1,10)
fdefen = 11 + random.randint(1,5)
fdam = random.randint(1,8)

mhealth = 15 + random.randint(1,10)
mdefen = 14 + random.randint(1,5)
mdam = random.randint(1,8)

rhealth = 20 + random.randint(1,10)
rdefen = 7 + random.randint(1,5)
rdam = random.randint(1,12)


def easystats():
    if grade == 1:
        print("You are a fighter.\nThey specialize in combo building melee combat.\nFighters deal moderate damage, and have high health with moderate defense")
        print(f"Your stats are {fhealth} for your hp, {fdefen} and a random number from 1 to 8 for damage.")

    elif grade == 2:
        print("You are a mage.\nThey specialize in longer range magic combat, and have good utility.\nThey have low health with moderate damage and high defense.")
        print(f"Your stats are {mhealth} for your hp, {mdefen} and a random number from 1 to 8 for damage.")

    elif grade == 3:
        print("You are a rogue.\nThey specialize in stealth and ambush tactics from close to medium range.\nThey deal high damage, have moderate health, and a low defense")
        print(f"Your stats are {rhealth} for your hp, {rdefen} and a random number from 1 to 12 for damage.")

    else:
        print("please enter a valid input for stats!")


def medstats():
    if grade == 1:
        print("You are a fighter.\nThey specialize in combo building melee combat.\nFighters deal moderate damage, and have high health with moderate defense")
        print(f"Your stats are {fhealth} for your hp, {fdefen} and a random number from 1 to 8 for damage.")

    elif grade == 2:
        print("You are a mage.\nThey specialize in longer range magic combat, and have good utility.\nThey have low health with moderate damage and high defense.")
        print(f"Your stats are {mhealth} for your hp, {mdefen} and a random number from 1 to 8 for damage.")

    elif grade == 3:
        print("You are a rogue.\nThey specialize in stealth and ambush tactics from close to medium range.\nThey deal high damage, have moderate health, and a low defense")
        print(f"Your stats are {rhealth} for your hp, {rdefen} and a random number from 1 to 12 for damage.")

    else:
        print("please enter a valid input for stats!")


def hardstats():
    if grade == 1:
        print("You are a fighter.\nThey specialize in combo building melee combat.\nFighters deal moderate damage, and have high health with moderate defense")
        print(f"Your stats are {fhealth} for your hp, {fdefen} and a random number from 1 to 8 for damage.")

    elif grade == 2:
        print("You are a mage.\nThey specialize in longer range magic combat, and have good utility.\nThey have low health with moderate damage and high defense.")
        print(f"Your stats are {mhealth} for your hp, {mdefen} and a random number from 1 to 8 for damage.")

    elif grade == 3:
        print("You are a rogue.\nThey specialize in stealth and ambush tactics from close to medium range.\nThey deal high damage, have moderate health, and a low defense")
        print(f"Your stats are {rhealth} for your hp, {rdefen} and a random number from 1 to 12 for damage.")

    else:
        print("please enter a valid input for stats!")


if diff == 1:
    print(easystats)
elif diff == 2:
    print(medstats)
elif diff == 3:
    print(hardstats)