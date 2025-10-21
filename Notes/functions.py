#IC 1st function notes
#Set variable first then we define all of our functions
player_health = 100
monster_health = 100 #<--global variable
def damage(amount, turn): #<---\
    if turn =="player":
        return monster_health - amount, player_health
    else:
        return monster_health, player_health - amount #<----/local variables

monster_health, player_health = damage(10, "player")
print(f"Monster health: {monster_health}")
print(f"Player health: {player_health}")

def add(x, y):
    return x+y


def initials(name):
    names = name.split(" ")
    initials = " "
    for name in names:
        initials+=name[0]

    return initials

total = add(5,5)
print(total)
print(f"10+72 = {add(10,72)}")
x = 0
while x < add(3,9):
    print("duck")
    x+= 1

print("goose!")
print(initials("Isaac Covington"))