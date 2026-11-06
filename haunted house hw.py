charm = input("Do you carry a holy charm? (yes/no): ").lower()
bravery = int(input("Enter your bravery level (out of 100): "))
hide = input("Do you hide? (yes/no): ").lower()
luck = int(input("Enter your luck level (out of 100): "))

if charm == "yes":
    if bravery > 60:
        print("You defeat the ghost.")
    else:
        print("You faint.")
else:
    if hide == "yes":
        if luck > 40:
            print("The ghost misses you.")
        else:
            print("You get possessed.")
    else:
        print("The ghost catches you!")