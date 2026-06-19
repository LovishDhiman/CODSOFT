import random

print("=== ROCK PAPER SCISSORS GAME ===")

choices = ["rock", "paper", "scissors"]

user_choice = input("Enter rock, paper, or scissors: ").lower()

if user_choice not in choices:
    print("Invalid choice!")
else:
    computer_choice = random.choice(choices)

    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You Win!")

    else:
        print("Computer Wins!")