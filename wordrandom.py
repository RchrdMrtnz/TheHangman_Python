import random
num = random.randint(1, 3)


def wordrand(num):
    animals = ["bull", "birds", "cow", "chicken", "hen", "donkey", "goat", "horse",
               "pig", "rabbit", "sheep", "turkey", "goose", "prawn", "shrimp", "dolphin", "shark"]
    colors = ["white", "black", "gray", "yellow",
              "orange", "brown", "golden", "silver", "purple"]
    things = ["bucket", "carabiner", "corkscrew",
              "flashlight", "hammer", "padlock", "golden", "silver"]
    if num == 1:
        result = random.randint(0, 16)
        hanganimal = animals[result]
    elif num == 2:
        result = random.randint(0, 7)
        hanganimal = colors[result]
    elif num == 3:
        result = random.randint(0, 7)
        hanganimal = things[result]
    return hanganimal
