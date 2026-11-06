
flavor = input("What flavor do you want?")
scoops = int(input("How many scoops do you want?"  ))

def order_ice_cream(flavor,scoops):
    
    print(f"You have ordered {scoops} scoops of {flavor} ice cream.")
    cost = scoops*20
    print(f"The total cost of your order is {cost}.")

order_ice_cream(flavor,scoops)
