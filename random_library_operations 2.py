#rock paer scissors... best of 3
import random

player_score = 0
comp_score = 0
options = ["rock" , "paper" , "scissors"]

print("Rock Paper Scissors Game... Best of 3 ")

while player_score < 2 and comp_score < 2:
    comp_choice = random.choice(options)
    player_choice = input("Choose from rock , paper scissors: ").lower()

    print(f"{player_choice} VS {comp_choice}")

    if player_choice == comp_choice:
        print("It's a Tie")

    elif (player_choice == "rock" and comp_choice == "scissors") or\
        (player_choice == "paper" and comp_choice == "rock") or\
        (player_choice == "scissors" and comp_choice == "paper"):
        player_score += 1
        print("Payer Wins")
    
    else:
        comp_score += 1
        print("Computer Wins")

    print(f"Score: Player : {player_score} | Computer : {comp_score}")

if player_score >= 2:
    print("\n Player Wins")

else:
    print("\n computer Wins")