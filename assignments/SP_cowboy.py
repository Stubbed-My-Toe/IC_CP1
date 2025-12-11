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
        B_defen:70
    },
    "Grenadier":{
        B_health:110,
        B_dodge:40,
        B_carry:190,
        B_accur:80,
        B_stren:80,
        
    }
}