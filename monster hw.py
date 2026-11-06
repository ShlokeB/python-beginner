import random

health = 100
coins = 50

print("You face a scary monster!")
print("1. Fight the monster")
print("2. Run away")
print("3. Bribe the monster")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    luck = random.choice(["win", "lose"])
    if luck == "win":
        print("You fought bravely and defeated the monster!")
    else:
        health -= 40
        print("You lost the fight and got injured.")
        print("Health left:", health)

elif choice == "2":
    health -= 20
    print("You ran away safely, but lost some health.")
    print("Health left:", health)

elif choice == "3":
    if coins >= 20:
        coins -= 20
        print("You bribed the monster and stayed safe.")
        print("Coins left:", coins)
    

else:
    print("Invalid choice. Please enter 1, 2, or 3.")
