#IC 1st Final Project: SP Cowboy

#will be a rogue-like where the player can pick up items and upgrades and eventually get to the boss to fight them.

#import random
#import time

#############################################################################################################################################

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



#############################################################################################################################################

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


#############################################################################################################################################

#ROOMS
    #Rooms come in 7 classes.