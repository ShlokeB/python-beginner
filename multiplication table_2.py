num = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

for a in range (num,num2+1):
    print(f"Table of {a}")
    for i in range(1,11):
        print (f" {a} * {i} = {a*i} ")

