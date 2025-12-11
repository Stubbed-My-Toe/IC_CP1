#IC 1st SP cowboy final project

import random
import time


#Classes and stats
B_dodge=int()
B_health=int()
B_accur=int()
B_defen=int()
B_carry=int()
B_stealth=int()
B_stren=int()
B_damage=int()

classes = {
    "Guerilla":{
        B_health:50,
        B_defen:70,
        B_dodge:80,        
        B_carry:120,
        B_accur:60,
        B_stren:110,
        B_stealth:65
    },
    "Gunslinger":{
        B_health:70,
        B_defen:70,
        B_dodge:50,
        B_carry:150,
        B_accur:100,
        B_stren:70,
        B_stealth:0
    },
    "Grenadier":{
        B_health:110,
        B_defen:80,
        B_dodge:40,
        B_carry:190,
        B_accur:80,
        B_stren:80,
        B_stealth:0
    }
}

while True:
    chosen_class = int(input("What class do you want to play? Type 1 for Guerilla, type 2 for Gunslinger, type 3 for Grenadier, and type 4 (doesn't work yet, just ask Isaac for more info on classes and stats) for more info.\n")).strip()

    if chosen_class == 1:
        class_are_you_sure=int(input("Are you sure? Once you selct this class you cannot change it at any time. Type 1 to continue with your selection, type 2 to go back and pick a different character.\n")).strip()
        if class_are_you_sure == 1:
                player_stats ={
                    B_health: classes["Guerilla"][B_health],
                    B_defen: classes["Guerilla"][B_defen],
                    B_dodge: classes["Guerilla"][B_dodge],
                    B_carry: classes["Guerilla"][B_carry],
                    B_accur: classes["Guerilla"][B_accur],
                    B_stren: classes["Guerilla"][B_stren],
                    B_stealth: classes["Guerilla"][B_stealth]
                },
                break
        else:
              continue
        
    elif chosen_class == 2:
        class_are_you_sure=int(input("Are you sure? Once you selct this class you cannot change it at any time. Type 1 to continue with your selection, type 2 to go back and pick a different character.\n")).strip()
        if class_are_you_sure == 1:
                player_stats ={
                    B_health: classes["Gunslinger"][B_health],
                    B_defen: classes["Gunslinger"][B_defen],
                    B_dodge: classes["Gunslinger"][B_dodge],
                    B_carry: classes["Gunslinger"][B_carry],
                    B_accur: classes["Gunslinger"][B_accur],
                    B_stren: classes["Gunslinger"][B_stren],
                    B_stealth: classes["Gunslinger"][B_stealth]
                },
                break
        else:
              continue
        
    elif chosen_class == 3:
    
        class_are_you_sure=int(input("Are you sure? Once you selct this class you cannot change it at any time. Type 1 to continue with your selection, type 2 to go back and pick a different character.\n")).strip()
        if class_are_you_sure == 1:
                player_stats ={
                    B_health: classes["Grenadier"][B_health],
                    B_defen: classes["Grenadier"][B_defen],
                    B_dodge: classes["Grenadier"][B_dodge],
                    B_carry: classes["Grenadier"][B_carry],
                    B_accur: classes["Grenadier"][B_accur],
                    B_stren: classes["Grenadier"][B_stren],
                    B_stealth: classes["Grenadier"][B_stealth]
                }
                break
        else:
              continue
    
    elif chosen_class==4:
        continue
    
    else:
        continue
exit

#Combat things

#Items (Just the baseline for now)
"Basic Revolver"={
    B_damage:25
}