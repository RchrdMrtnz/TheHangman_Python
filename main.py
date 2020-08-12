import os
import time
import random
from wordrandom import wordrand
from difficulty import difficulty
from game import game
from title import title

title()
os.system(
    'read -s -n 1 -p "\nOnly silly children become hanged, now press any key \n"')
time.sleep(0.2)
try:
    level = int(input(
        "Now is the time to prove that you are not a fool, choose the level from 1 to 3:  "))
except:
    print("only 1 or 2 or 3 \n".center(140))
    level = int(
        input(" you are a fool, choose again the level from 1 or 2 or 3 \n"))
lifes = difficulty(level)

game(lifes)

goback = input("\nDo you want to try again useless? Y/N\n")

if goback == "y" or goback == "Y" or goback == "yes" or goback=="YES":
    while goback == "y" or "Y" or "yes":
        title()
        vidas = 10
        game(lifes)
        goback = input("Do you want to try again useless? Y/N \n")
        if goback == "y" or goback == "Y" or goback == "yes" or goback=="YES":
            pass
        elif goback == "n" or goback == "N" or goback == "not" or goback == "NOT":
            break

elif goback == "n" or goback == "N" or goback == "not" or goback == "NOT":
    print("are you a chicken?\nThis is not for cowards")
    time.sleep(0.5)
