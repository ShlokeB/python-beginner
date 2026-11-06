def buy_ticket():
    age = int(input("Please enter your age: "))
    money = int(input("Please enter the amount of money you have: "))
    if age <= 5:
        print("You get a free ticket!")
    elif age <=12:
        print("You can buy a ticket for 10.")
        if money >= 10:
            print("You have enough money to buy the ticket.")       
        elif money < 10:
            print("You do not have enough money to buy the ticket.")
    elif age >12:
        print("You can buy a ticket for 20.")
        if money >= 20:
            print("You have enough money to buy the ticket.")       
        elif money < 20:
            print("You do not have enough money to buy the ticket.")
    
buy_ticket()