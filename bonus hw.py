r = float(input("Enter the employee performance rating from 1-5"))
if r>=1 and r<2:
    print("You have no bonus")
elif r>2 and r<=3.5:
    print("Your bonus is 10% of your salary")
elif r>3.5 and r<=4.5:
    print("Your bonus is 20% of your salary")
elif r>4.5:
    print("Your bonus is 30% of your salary")
    