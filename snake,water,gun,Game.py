# Snake, Water, Gun Game
"""
snake => drink water,
water => destroy gun,
gun=> kills snake
"""
import random

# Mapping user inputs and outcomes
choices = {"s": 1, "w": -1, "g": 0}
reverse_choices = {1: "Snake", -1: "Water", 0: "Gun"}

# Getting user input
user_input = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
# Validating user input
if user_input not in choices:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    user_choice = choices[user_input]
    
    # Random computer choice
    computer_choice = random.choice([-1, 0, 1])
    
    print(f"\nYou chose: {reverse_choices[user_choice]}")
    print(f"Computer chose: {reverse_choices[computer_choice]}\n")
    
    # Logic for deciding the winner
    if user_choice == computer_choice:
        print("It's a DRAW!")
    elif (user_choice == 1 and computer_choice == -1) or \
        (user_choice == -1 and computer_choice == 0) or \
        (user_choice == 0 and computer_choice == 1):
        print("You WIN!")
    else:
        print("You LOSE!")
