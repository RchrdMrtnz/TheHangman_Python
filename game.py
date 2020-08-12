import os
import time
import random
from wordrandom import wordrand
from difficulty import difficulty
from record import *      
def game(lifes):
    num = random.randint(1, 3)
    word = wordrand(num)
    yourword= " "
    counter = 0
    the_hang_text = ["\n________", "|/      |", "|       |", "|      (_)", "|      _|/", "|       |", "|      /|", "|        ", "|        ", "|____________"]
    while lifes > 0:
        try:
            lower_case = input(
                " \n Enter a letter, if you have the courage:  ")[0]
        except:
            print(
                "\n Only letters dont be a don't be a cheater, no numbers or empty spaces")
            lower_case = input("Try again \n")
        letter = lower_case.lower()
        yourword += letter  
        fails = 0
        for letters in word:
            if letters in yourword:
                print(letters, end="")
            else:
                print("*", end="")
                fails += 1
        if fails == 0:
            print("\n Congratulations, you're not a fool ... totally")
            record()
            print("Hall Of Fame\n")
            leer()
            break
        if (lifes > 0) and (letter not in word):
            counter += 1
            for i in range(counter):
                counter_animation = int(i)
                if counter_animation < 8:
                    print(the_hang_text[counter_animation])
                elif counter_animation == 9 or counter_animation == 10:
                    counter_animation=8
                    print(the_hang_text[counter_animation])
                    print(the_hang_text[8])
                elif counter_animation == 11:
                    counter_animation=9
                    print(the_hang_text[counter_animation])
                counter_animation+1
                time.sleep(0.3)
        if letter not in word:
            lifes -= 1
            print("\n How pathetic, you failed \n")
            print(f"Do you have {lifes} lifes")
        if lifes == 0:
            print(f"Seriously? you could not guess \"{word}\" \n")
            print("You lost, from now on your neck won't be the same, idiot \n")
    else:
        print("Thanks for wasting my time \n")
        time.sleep(0.2)
    return lifes
