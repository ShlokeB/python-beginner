balance = 5000

while True:
    print("ATM Menu")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    option = input("Choose an option (1-4): ")

    if option == "1":
        print(f"Your balance is ₹{balance}")
    elif option == "2":
        amount = input("Enter amount to deposit: ")
        if amount.isdigit():
            balance += int(amount)
            print(f"₹{amount} deposited. New balance is ₹{balance}")
        else:
            print("Invalid amount")
    elif option == "3":
        amount = input("Enter amount to withdraw: ")
        if amount.isdigit():
            amount = int(amount)
            if amount <= balance:
                balance -= amount
                print(f"₹{amount} withdrawn. Remaining balance is ₹{balance}")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid amount")
    elif option == "4":
        print("Exiting the app.....")
        break
    else:
        print("Invalid Option")
