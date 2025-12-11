#IC 1st SP cowboy final project

import random
import time



B_dodge=int()
B_health=int()
B_accur=int()
B_defen=int()
B_carry=int()
B_stealth=int()
B_stren=int()

classes = {
    "Guerilla":{
        B_dodge:80, 
        B_health:50,
        B_defen:70,
        B_carry:120,
        B_accur:60,
        B_stren:110,
        B_stealth:65
    },
    "Gunslinger":{
        B_health:70,
        B_carry:150,
        B_dodge:50,
        B_accur:100,
        B_stren:70,
        B_defen:70,
        B_stealth:0
    },
    "Grenadier":{
        B_health:110,
        B_dodge:40,
        B_carry:190,
        B_accur:80,
        B_stren:80,
        B_defen:80,
        B_stealth:0
    }
}

def character_creation():
    

chosen_class = int(input("What class do you want to play? Type 1 for Guerilla, type 2 for Gunslinger, type 3 for Grenadier, and type 4 for more info.\n")).strip()

if chosen_class == 1:
    class_are_you_sure=int(input("Are you sure? Once you selct this class you cannot change it at any time. Type 1 to continue with your selection, type 2 to go back and pick a different character.\n")).strip()
    if class_are_you_sure == 1:
        player_name="Guerilla"
        player_health = ""



