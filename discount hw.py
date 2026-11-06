amount = int(input("Please enter the total purchase amount in INR: "))
if amount<= 500:
    print(f"Final price in INR is: {amount:.2f}")
elif amount>500 and amount <=2000:
    print(f"Final price in INR is: {(amount*90/100):.2f}")
elif amount >2000 and amount<=5000:
    print(f"Final price in INR is: {(amount*85/100):.2f}")
elif amount>5000:
    print(f"Final price in INR is: {amount*4/5:.2f}")

    