"""⭐ Q4. Shopping Bill Calculator
Create a function called bill().
Ask the user to enter prices of 5 items.
Use a loop to calculate the total bill.
If total bill exceeds ₹1000:
* Give a 10% discount.
Display:
* Total Bill
* Discount
* Final Amount"""

def bill():
    total =0
    for i in range(5):
        price=int(input("Enter the price: "))
        total+=price
    print(total)
    if total>1000:
        final_price = total * (9/10)
        discount=(10/100)*total
    else:
        final_price=total
        discount=0
    print("Price is", (total))
    print(f"Discount is: {discount:.2f}")
    print(f"Final price is: {final_price:.2f}")
    
    



bill()


