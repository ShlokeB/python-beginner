import random

shelter = random.choice(["yes", "no"])

if shelter == "yes":
    water = random.choice(["yes", "no"])

    if water == "yes":
        food = random.choice(["yes", "no"])

        if food == "yes":
            fire = random.choice(["yes", "no"])

            if fire == "yes":
                print("You survive comfortably.")
            else:
                print("Cold is dangerous.")
        else:
            fish = random.choice(["yes", "no"])

            if fish == "yes":
                print("You catch fish.")
            else:
                print("You become weak.")
    else:
        rain = random.choice(["yes", "no"])

        if rain == "yes":
            print("You collect rainwater.")
        else:
            print("You become dehydrated.")
else:
    animals = random.choice(["yes", "no"])

    if animals == "yes":
        weapons = random.choice(["yes", "no"])

        if weapons == "yes":
            print("You scare them away.")
        else:
            print("The animals attack you.")
    else:
        boat = random.choice(["yes", "no"])

        if boat == "yes":
            print("You escape the island!")
        else:
            print("You remain stranded.")