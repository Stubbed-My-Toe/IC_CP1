#IC 1st Combat Activity Diagram

import random
print("Welcome to the combat program.\n I ask that you give me your name and specialties before we start.")
name = input("What is your name?\n")
grade = int(input("Press 1 if you are a fighter, 2 if you are a mage, and 3 if you are a rogue.\n"))
diff = int(input("What is your desired difficulty of combat? Press 1 for easy, 2 for medium, and 3 for hard.\n"))

def stats():
    if grade == 1:
        print("You are a fighter.\nThey specialize in combo building melee combat.\nFighters deal moderate damage, and have high health with moderate defense")
        
    elif grade == 2:
        print("You are a mage.\nThey specialize in longer range magic combat, and have good utility.\nThey have low health with moderate damage and high defense.")
    elif grade == 3:
        print("You are a rogue.\nThey specialize in stealth and ambush tactics from close to medium range.\nThey deal high damage, have moderate health, and a low defense")

