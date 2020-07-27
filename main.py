import time
import random
from wordrandom import wordrand
from difficulty import difficulty
from game import game
from title import title

title()
start = input(
    "Only silly children become hanged, Now press enter to dead \n".center(140))
time.sleep(0.2)
try:
    level = int(input(
        "Now is the time to prove that you are not a fool, choose the level from 1 to 3".center(140)))
except:
    print("only 1 or 2 or 3\n".center(140))
    level = int(
        input(" you are a fool, choose again the level from 1 or 2 or 3 \n".center(140)))
lifes = difficulty(level)

game(lifes)

goback = input("Do you want to try again useless? Y/N")
while goback == "y":
    title()
    vidas = 10
    game(lifes)
    goback = input("Do you want to try again useless? Y/N \n")
