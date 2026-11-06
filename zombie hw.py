safe = input("Are you inside a safe house? (yes/no): ").lower()
food = input("Do you have food? (yes/no): ").lower()
weapons = input("Do you have weapons? (yes/no): ").lower()
car = input("Do you have a car? (yes/no): ").lower()
fuel = int(input("Enter fuel level: "))

if safe == "yes":
    if food == "yes":
        if weapons == "yes":
            print("You survive the night safely.")
        else:
            print("You are safe, but still vulnerable.")
    else:
        print("You starve.")
else:
    if car == "yes" and fuel > 50:
        print("You escape the city.")
    else:
        print("Zombies catch you!")