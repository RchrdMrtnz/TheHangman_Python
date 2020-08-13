import os
import time
import random
from wordrandom import wordrand
from difficulty import difficulty
from record import leer, record     
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
            see_records=input("if you wanna see the famous table press 1")
            if see_records=="1":
                leer()
            break
        if (lifes > 0) and (letter not in word):
            counter+= 1
            for i in range(counter):
                if i < 8:
                    print(the_hang_text[i])
                elif i >= 9:
                    print(the_hang_text[8])
                time.sleep(0.3)
        if letter not in word:
            lifes -= 1
            print("\nHow pathetic, you failed \n")
            print(f"Do you have {lifes} lifes \n")
        if lifes == 0:
            time.sleep(1.2)
            print(f"Seriously? you could not guess \"{word}\" \n")
            time.sleep(1.5)
            print("You lost, from now on your neck won't be the same, idiot \n")
            time.sleep(1.2)
            print("you are dead man")
            time.sleep(1.2)
            for i in range(0,10):
                print(the_hang_text[i])
                time.sleep(0.5)
    else:
        print("\nThanks for wasting my time \n")
        time.sleep(0.2)
        see_records=input("if you wanna see the famous table press 1 ")
        if see_records=="1":
            leer()
    return lifes
if __name__ == "__main__":
    lifes=1
    game(lifes)
