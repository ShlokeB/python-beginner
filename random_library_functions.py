import random
secret_number = random.randint(1, 100)
attempts = 0

while attempts < 10:
    guess = int(input("Enter a number: "))
    attempts += 1

    if guess == secret_number:
        print(f"You guessed the number in {attempts} attempt(s).")
        break
    elif guess < secret_number:
        print("Too low, try a higher number")
    elif guess > secret_number:
        print("Too high, try a lower number")

    print(f"You have  {10 - attempts} attempts left")

if attempts == 10:
    print("Game Over!!!")
    print("The number was ", secret_number)