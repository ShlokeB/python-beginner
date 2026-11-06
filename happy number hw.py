num = int(input("Enter a number: "))
original = num
list= []
while num != 1 and num not in list:
    list.append(num)
    total=0
    while num>0:
        digit=num%10 #2nd digit
        total+=digit**2
        num=num//10 #1st digit
    num=total
if num==1:
    print("Happy Number")
else:
    print("Not happy number")

    