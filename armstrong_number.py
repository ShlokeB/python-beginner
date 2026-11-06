num = int(input("Enter a number: "))
digits = len(str(num))
original=num

total=0
while num>0:
    digit=num%10 #2nd digit
    total+=digit**digits
    num=num//10 #1st digit

if total==original:
    print("Armstrong Number")
else:
    print("Not armstrong number")

    