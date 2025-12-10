#IC 1st Final Project: SP Cowboy

#will be a rogue-lite where the player can pick up items and upgrades and eventually get to the boss to fight them.
#inspired by titles such as borderlands, fallout, and rogue

#import random
import random
#import time
import time



#PART 1: THE DESIGNING OF STATS AND FUNCTIONS
#############################################################################################################################################################################################################################################################################################################

#STATS FOR SURVIVAL
    #These make sure that the player does not die instantly, or so the player can get really strong. Are meant to be unbalanced.


    #HEALTH
        #Health is 70 at base for character creation, with exceptions for 2 classes
B_health = 70
        #Determines if the player will die to certain attacks, will be called grit in actual gameplay


    #DEFENSE
        #defense is 70 at base. It is the ability to tank shots without bleeding or taking any actual damage.
B_defen = 70
        #If armor plates are picked up, they will affect weight. The more armor that is carried, the more weight is added.
        #Determines if the player will be able to block attacks without taking damage. Will be called gumption in actual gameplay.
        

    #DODGE
        #Ducking behind barrels, moving quick and good a good eye can keep the player from getting hurt. Strts at 50, goes up with certain classes.
B_dodge = 50
        #Things like dodging and ducking in rooms, moving fast and being shifty. Called speed in actual gameplay.


    #CARRY
        #determines how much the player can lift. Starts at 150 but can go up with upgrades and certain classes' abilities.
B_carry = 150
        #Determines how much the player can lift. will sort of work like the weight function in fallout. Too much weight (70% of max) leads to a decrease in speed. 100% of weight or over will lead to the character taking a huge hit to speed. Called mule in gameplay.
    

    #STEALTH
        #The stealth stat determines if the player can get past certain interactions with enemies and NPCs
        #If stealth is higher than an enemies stealth stat, they will most likely not be noticed and will have the advantage to perform a special action on their enemy.
        #Guerilla is the only class that starts with stealth


###########################################################################################################################################################################################################################################################################################################

#3 CLASSES 
classes = {
    #with different stats like dodge, health, defense and carry weight


    #Guerilla (only one with stealth at base)
    "Guerilla" : {B_dodge:80,}
        #Very stealthy and melee focused in combat. Can still use guns, especially those with stealth aspects.
        #Pretty fast, but low health and carry weight.
        #Has stealth attacks.
            #Stealth attacks do 1.5 damage at base, can be increased with some items.
            #Can be activated in combat if the enemy's defense stat is not as high as the speed stat
        #Has a base health of 50
        #Has a dodge of 80 at base
        #Defense of 70 at base
        #Carry starts at 120, with accuracy at 60, strength at 110


    #Gunslinger (stereotypical cowboy)
        #Is average in speed, but is proficient in guns. Pretty decent health
        #Carry weight is pretty good, but a stat called "dexterity" allows them to move more quickly when carrying heavy stuff.
        #Has special action called "quick draw" which allows them to fire very quickly.
            #quickdraw: Allows the player to get the bonus of 2 shots in on guns per turn
        #70 base health, Carry weight is 150 but has a overload weight of 80%, dodge is 50 at base, with accuracy at 100, and strength at 50.

    #Grenadier (Big boom guy)
        #The Tank of the classes. Due to using explosives, they have developed to be very strong which positively affects carry weight
        #Can craft and use explosives, as well as being able to carry a surplus of explosives.
        #High health, low speed. Very noticeable.
        #Health starts at 110, and dodge is at 30, and carry is 190, and accuracy is 80, and strength at 80, and defense is at 80.
}

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
                #Will have a fuction that determines if the enemy is close at all, if so, they will take tons of damage.

            #IMPROVISED
                #This is like stabbing someone with a table leg, or throwing a fork. It works?
                #Made by doing things like breaking chairs.


    #IMPLANTS
        #Stuff like coal powered arms.
        #These can be put on and off only in rest rooms.
        #They provide bonuses to physical stats and some provide powers.


    #CONSUMABLES
        #Ammo, bandages, armor, and anything that can be consumed in some way.
        #These will be used and not be able to be unused. Ammo will be consumed on firing, bandages, on healing, and etc.


    #VALUABLES
        #Pretty much anyhting can be sold. These are meant to be sold and used to buy things.
        #Can be sold to merchants for money.


###########################################################################################################################################################################################################################################################################################################

#STATS FOR COMBAT
    #These are stats that directly affect combat scenarios.


    #DAMAGE
        #There are a few types of damage that are dealt by different weapons.
        #Attack means the player will want to do some form of damage to the enemy.
        #If the attack is not guaranteed to hit, it will pass through the accuracy check. If the accuracy stat is not as high as the enemies dodge stat, the player will not be able to hit them.
        #The damage variable will be used and passed through whatever function the attack is.
        #This will determine if the player will be able to hit.

        #MELEE
            #The player attacks, if their strength is high enough, they can do quite a bit of damage. (Guaranteed to hit)
            #The player actually has to get close enough to hit them, so they need to pass a dodge check
            #If dodge check is passed, the player can hit the enemy and will stay in range unless the enemy decides to back up. If failed, the player will be at the mercy of a counter-attack by the enemy.
            #When in range, the player will always hit their melee attack


    #ACCURACY
        #Determines if the player will hit where they want to hit.
        #Will usually be determined by the player *accuracy* stat. Some guns have accuracy stats that just add to the player's accuracy stat.
        #If the player does a ranged attack, their accuracy stat comes into play.
        #There is the  base accuracy stat and the rolled accuracy stat. The rolled accuracy is added to the base accuracy.
        #If the enemy has a dodge stat that is higher than the accuracy stat, they will not be hit by the attack.


    #STRENGTH
        #Affects how much damage the player will do for melee attacks.
        #Strength is divided by 5 and then added onto the weapon's damage.


###########################################################################################################################################################################################################################################################################################################

#ROOMS
    #Rooms come in 6 classes.
    #They are randomly selected, but some have lower chances of showing up
    #Enemies can spawn in any room except r&m rooms and merchant rooms.
    #Boss rooms require tickets*
    #The rooms will be randomly generated, and when entered, the room number will get put on a list, which determines the order of the rooms.

    #LOOT ROOMS
        #These have weapons, loot, and armor as well as special items in them.
        #These have a few locations where the items have numbers assigne to them that the randomizer is going to find it in a list and put it there.

    #FIGHT ROOMS
        #As the name suggests these are rooms with enemies specifically designed for combat. Enemies will mostly be encountered in these rooms.
        #Enemies can spawn here, but there are still a few locations where loot can spawn.

    #MERCHANT ROOMS
        #This is where currency is used to buy items such as implants, weapons, and protection
        #*The merchants have something called boss tickets. These will take players to boss rooms if used.

    #BOSS ROOMS
        #Rooms where bosses will be encountered and fought.
        #The tickets will be connected to functions that when activated will take tthe player to the room

    #REST & MAINTENANCE ROOMS
        #Where the player can rest, and recover. Enemies cannot spawn here. If the player dies, they will show back up at their most recent r&m room, but missing their most powerful weapon (implants do not count) and at 1/2 health.
        #Each weapon has a score assigned based on stats. the item with the highest score will be deleted.

    #TRAP ROOMS
        #Trap rooms are rooms that can contain enemies and a little loot. They will show up as a fight room, but will have traps in them.
        #The traps will be things like strings connected to gold coins, and floorboards that fall through.


###########################################################################################################################################################################################################################################################################################################

#ENEMIES
    #Enemies come in a few different variants.

    #BOSSES
        #The big bads
        #They are big and evil.
        #With lots of health, abilities and more.
        #On death, random items will be chosen and dropped

    #FODDER
        #The meh enemies, basic revolvers and items, but still dangerous
        #Spawn the most commonly in the game.
        #Will have the same stats as the player, but only a few abilities called 'shoot', and other basic names and and basic melees.
        #Each attack is chosen at random, but in melee they will only do melee

    #SPECIALS
        #Guys with special weapons, and based off of the classes.
        #Class they are based off of will be randomly assigned.
        #If one class is chosen, they will specifically do only certain moves that make sense for that class.
        #Nearly exactly like the player but will be randomly assigned a ranged and melee weapon of a certain score range.

    #ELITE VARIANTS
        #Variants of enemies, but way more busted than the originals.
        #Gain special abilities such as only doing fire damage. 
        #Will be given higher tier loot.


###########################################################################################################################################################################################################################################################################################################

#THE CYLINDER (It looks like a revolver barrel)
    #This might be the most important thing in the entire game.
    #Every room that is visited, the cylinder will go down one bullet.
    #Every bullet that dissapears, enemies gain +2% to all their stats.
    #Every 2 bullets that dissapear allows the player to increase the strength of a stat or power slightly.
    #When the last bullet dissapears, the enemies gain +10% to their stats, but the player gets to 'draw' an ability that is chosen at random.