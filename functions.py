import math


def sum(a, b):
    s = a + b
    print(f"Sum = {s}")

def minus(a, b):
    sub = a - b
    print(f"Difference = {sub}")

def multiply(a, b):
    m = a * b
    print(f"Product = {m}")

def divide(a, b):
    d = a / b
    print(f"Quotient = {d}")

def square(a):
    sq = a ** 2
    print(f"Square = {sq}")

def squareroot(a):
    ans = math.sqrt(a)
    print(f"Square root = {ans}")


while True:
    print("Calculator App")
    print("=============")
    a = (input("Enter a number: "))
    b = (input("Enter a number: "))
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Square Root")
    print("7. Exit")
    op = int(input("Enter a operator (1-7): "))
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        if op == 1:
            sum(a, b)
        elif op == 2:
            minus(a, b)
        elif op == 3:
            multiply(a, b)
        elif op == 4:
            if b == 0:
                print("Cannot divide by zero")
            else:
                divide(a, b)
        elif op == 5:
            square(a)
        elif op == 6:
            squareroot(a)
        elif op == 7:
            print("Exiting the app.....")
            break
        else:
            print("Invalid Option")
        