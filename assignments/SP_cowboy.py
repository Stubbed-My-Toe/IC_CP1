#IC 1st SP cowboy final project

import random
import time


#Classes and stats
M_health = "max health"
C_health = "current health"
def health():
    if C_health <= M_health:
        print(f"{C_health}/{M_health} hp")
    elif C_health > M_health:
        C_health-=(C_health-M_health)
    else:
        print("Idk how you did this one. Get my help I guess?")

C_defen = "current defense"
C_dodge = "current dodge"
M_carry = "max carry weight"
C_carry = "current carry weight"
C_accur = "current accuracy"
C_stealth = "current stealth"
C_stren = "current strength"
C_damage = "damage"
money = int()

classes = {
    "Guerilla":{
        M_health:60,
        C_defen:70,
        C_dodge:80,        
        M_carry:120,
        C_accur:60,
        C_stren:110,
        C_stealth:65
    },
    "Gunslinger":{
        M_health:80,
        C_defen:70,
        C_dodge:50,
        M_carry:150,
        C_accur:100,
        C_stren:70,
        C_stealth:0
    },
    "Grenadier":{
        M_health:100,
        C_defen:80,
        C_dodge:40,
        M_carry:190,
        C_accur:80,
        C_stren:80,
        C_stealth:0
    }
}

while True:
    chosen_class = int(input("What class do you want to play? Type 1 for Guerilla, type 2 for Gunslinger, type 3 for Grenadier, and type 4 (doesn't work yet, just ask Isaac for more info on classes and stats) for more info.\n")).strip()

    if chosen_class == 1:
        class_are_you_sure=int(input("Are you sure? Once you selct this class you cannot change it at any time. Type 1 to continue with your selection, type 2 to go back and pick a different character.\n")).strip()
        if class_are_you_sure == 1:
                name = "Guerilla"
                player_stats ={
                    M_health: classes["Guerilla"][M_health],
                    C_defen: classes["Guerilla"][C_defen],
                    C_dodge: classes["Guerilla"][C_dodge],
                    M_carry: classes["Guerilla"][M_carry],
                    C_accur: classes["Guerilla"][C_accur],
                    C_stren: classes["Guerilla"][C_stren],
                    C_stealth: classes["Guerilla"][C_stealth],
                    money: 0
                },
                break
        else:
            print("Going back.")
            continue
        
    elif chosen_class == 2:
        class_are_you_sure=int(input("Are you sure? Once you selct this class you cannot change it at any time. Type 1 to continue with your selection, type 2 to go back and pick a different character.\n")).strip()
        if class_are_you_sure == 1:
                name = "Gunslinger"
                player_stats ={
                    M_health: classes["Gunslinger"][M_health],
                    C_defen: classes["Gunslinger"][C_defen],
                    C_dodge: classes["Gunslinger"][C_dodge],
                    M_carry: classes["Gunslinger"][M_carry],
                    C_accur: classes["Gunslinger"][C_accur],
                    C_stren: classes["Gunslinger"][C_stren],
                    C_stealth: classes["Gunslinger"][C_stealth],
                    money:0
                },
                break
        else:
            print("Going back.")
            continue
        
    elif chosen_class == 3:
        class_are_you_sure=int(input("Are you sure? Once you selct this class you cannot change it at any time. Type 1 to continue with your selection, type 2 to go back and pick a different character.\n")).strip()
        if class_are_you_sure == 1:
                name = "Grenadier"
                player_stats ={
                    M_health: classes["Grenadier"][M_health],
                    C_defen: classes["Grenadier"][C_defen],
                    C_dodge: classes["Grenadier"][C_dodge],
                    M_carry: classes["Grenadier"][M_carry],
                    C_accur: classes["Grenadier"][C_accur],
                    C_stren: classes["Grenadier"][C_stren],
                    C_stealth: classes["Grenadier"][C_stealth],
                    money:0

                }
                break
        else:
            print("Going back.")
            continue
    
    elif chosen_class==4:
        continue
    
    else:
        continue

print("\nClass selected:", name)
print("Stats:", player_stats)


#Weight system
def pickup(item):
    player_stats[C_carry] += item["weight"]

def use(item):
     player_stats[C_carry] -= item["weight"]

#Items (Just the baseline for now)
Basic_Revolver={
    C_damage:26,
    C_accur:15,
    "weight":3,
    "capacity":6
}
Trench_Club={
    C_damage:30,
    "weight":4
}
Carbine={
    C_damage:34,
    C_accur:20,
    "weight":7,
    "capacity":10

}

def ammo():
    if C_damage == True:
        ammo-=1

Health_Potion={
    "heal" : 45,
    "weight" : 2.5,
    "ID" : 1,
    "Price" : 45
}
def healing():
    player_stats[C_health] += Health_Potion["heal"]

armor={
    "defense" : 30,
    "ID" : 2,
    "price" : 20
}
def apply_armor():
    player_stats[C_defen]+= armor["defense"]

Weapons=[Basic_Revolver, Carbine, Trench_Club]
Consumables=[ammo, armor, Health_Potion, money]

#Inventory
max = player_stats[M_carry]
current_weight = player_stats[C_carry]
def max_carry():
    if C_carry > M_carry:
        print("You are overencumbered! Drop an item or suffer mobility consequences.")
    else:
        print(f"{C_carry}/{M_carry}")




#ENEMIES
Basic_enemies={
    "Weapon": Basic_Revolver,
    M_health: 50,
    C_health: 50,
    C_defen: 60,
    C_dodge:50,
    C_accur: 40,
    C_stealth:40,
    C_stren:30
}


#ROOMS
loot_locations = ["Left Corner", "Right Corner", "Upper Shelf", "Lower Shelf", "Basket", "Cabinet", "Crate", "Chest", "Desk"]
#Loot rooms
Loot_rooms={
    "Description": "A dusty room, with cobwebs in the corners. From where you stand, you can see some loot lying around the room.",
    "Enemies":2,
    "Loot":5
}
#fight rooms
Fight_rooms={
    "Description":"A dark, musty room, bullet casings littering the floor. Many have come here recently, but you get a feeling not many have left.",
    "Enemies":4,
    "Loot": 2
}
#Merchants
for_sale={
    "armor_plates" :{
        "price":20,
        "action":apply_armor
        },
    "Healing Potion": Health_Potion
    
}
def merchant(purchase,money):
    while merchant==True:
        print("*As you enter the room, a friendly-looking merchant waves for you to come over.*\n Merchant: Welcome to my humble shoppe! Please respect the merchandise!")
        purchase = input(print(for_sale.items()))
        print('Type the name of the item you would like to purchase and hit enter')
        if purchase == True:
            print("Processing transaction")
            money =- for_sale["armor_plates"],["price"]
            if money <= 0:
                print("Transaction refused, you don't have enough money for this item")
        else:
            print("Get out of my shop")
                

#Combat things
Moves=[Health_Potion, apply_armor, "Attack"]

def player_turn():
    print(Moves)
    selected_move=input("what move do you want to do")
    if selected_move == Health_Potion:
        healing()
        exit
    elif selected_move== apply_armor:
        apply_armor()
        exit
    elif selected_move=="Attack" or "attack":
        attack_move = print("what move do you want to perform?", Weapons)
        if attack_move == Basic_Revolver:
            Basic_enemies[C_health]-=26
        elif attack_move == Carbine:
            Basic_enemies[C_health]-=34
        elif attack_move == Trench_Club:
            Basic_enemies[C_health]-=30

