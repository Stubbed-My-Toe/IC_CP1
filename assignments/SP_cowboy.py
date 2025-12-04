#IC 1st Final Project: SP Cowboy

#will be a rogue-lite where the player can pick up items and upgrades and eventually get to the boss to fight them.
#inspired by titles such as borderlands, fallout, and evil west

#import random
#import time


###########################################################################################################################################################################################################################################################################################################

#STATS FOR COMBAT
    #These are stats that directly affect combat scenarios.


    #DAMAGE
        #There are a few types of damage that are dealt by different weapons.
        

    #ACCURACY
        #Determines if the player will hit where they want to hit.

    #STRENGTH
        #affects how much damage the player will do for melee attacks.


###########################################################################################################################################################################################################################################################################################################

#STATS FOR SURVIVAL
    #These make sure that the player does not die instantly, or so the player can get really strong. Are meant to be unbalanced.


    #HEALTH
        #Health is 70 at base for character creation, with exceptions for 2 classes
        #Determines if the player will die to certain attacks, will be called grit in actual gameplay


    #DEFENSE
        #defense is 70 at base. It is the ability to tank shots without bleeding or taking any actual damage.
        #If armor plates are picked up, they will affect weight. The more armor that is carried, the more weight is added.
        #Determines if the player will be able to block attacks without taking damage. Will be called gumption in actual gameplay.
        

    #DODGE
        #Ducking behind barrels, moving quick and good a good eye can keep the player from getting hurt. Strts at 50, goes up with certain classes.
        #Things like dodging and ducking in rooms, moving fast and being shifty. Called speed in actual gameplay.


    #CARRY
        #determines how much the player can lift. Starts at 150 but can go up with upgrades and certain classes' abilities.
        #Determines how much the player can lift. will sort of work like the weight function in fallout. Too much weight (over 65% of max) leads to a decrease in speed. Called mule in gameplay.


###########################################################################################################################################################################################################################################################################################################

#3 CLASSES 
    #with different stats like dodge, health, defense and carry weight


    #Guerilla
        #Very stealthy and melee focused in combat. Can still use guns, especially those with stealth aspects.
        #Pretty fast, but low health and carry weight.
        #Has stealth attacks.


    #Gunslinger
        #Is average in speed, but is proficient in guns. Pretty decent health
        #Carry weight is pretty good, but a stat called "dexterity" allows them to move more quickly when carrying heavy stuff.
        #Has special action called "quick draw" which allows them to fire very quickly.


    #Grenadier
        #The Tank of the classes. Due to using explosives, they have developed to be very strong which positively affects carry weight
        #Can craft and use explosives, as well as being able to carry a surplus of explosives.
        #High health, low speed. Very noticeable.


###########################################################################################################################################################################################################################################################################################################

#ROOMS
    #Rooms come in 6 classes.
    #They are randomly selected, but some have lower chances of showing up
    #Enemies can spawn in any room except r&m rooms and merchant rooms.
    #Boss rooms are on a timer to appear. Every six rooms, a message will appear asking if the player wants to fight the boss.

    #LOOT ROOMS
        #These have weapons, loot, and armor as well as special items in them.

    #FIGHT ROOMS
        #As the name suggests these are rooms with enemies specifically designed for combat. Enemies will mostly be encountered in these rooms.

    #MERCHANT ROOMS
        #This is where currency is used to buy items such as implants, weapons, and protection

    #BOSS ROOMS
        #Rooms where bosses will be encountered and fought.

    #REST & MAINTENANCE ROOMS
        #Where the player can rest, and recover. Enemies cannot spawn here. If the player dies, they will show back up at their most recent r&m room, but missing their most powerful weapon (implants do not count) and at 1/2 health.

    #TRAP ROOMS
        #Trap rooms are rooms that can contain loot as well as enemies. They will show up as a fight room, but will have traps in them.


###########################################################################################################################################################################################################################################################################################################

#ITEMS
    #Items come in 4 categories: Weapons, Implants, Consumables, and Valuables.


    #WEAPONS
        #Weapons have 4 sub-categories: Projectile, Melee, Explosive, and Improvised; SUB-CATEGORIES GALORE!
            #PROJECTILE
                #These are the weapons that use bullets and anything that can fire far.

            #MELEE
                #Close quarters fighting.

            #EXPLOSIVE
                #BIG BOOM, VERY DANGEROUS

            #IMPROVISED
                #This is like stabbing someone with a table leg, or throwing a fork. It works?


    #IMPLANTS
        #Stuff like coal powered arms.


    #CONSUMABLES
        #Ammo, bandages, armor, and anything that can be consumed in some way.


    #VALUABLES
        #Pretty much anyhting can be sold. These are meant to be sold and used to buy things.


###########################################################################################################################################################################################################################################################################################################

#ENEMIES
    #Enemies come in a few different variants.

    #BOSSES
        #The big bads

    #FODDER
        #The meh enemies, basic revolvers and items, but still dangerous

    #SPECIALS
        #Guys with special guns, and based off of the classes

    #ELITE VARIANTS
        #Variants of enemies, but way more busted