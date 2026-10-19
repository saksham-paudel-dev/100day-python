import random

# ASCII art for the choices
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Storing the ASCII art inside a Python list
game_images = [rock, paper, scissors]

try:
    # Get user input
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

    # Check for valid range to prevent IndexError or handle it gracefully
    if user_choice < 0 or user_choice > 2:
        print("You typed an invalid number! You lose by default.")
    else:
        # Display user choice using list indexing
        print("You chose:")
        print(game_images[user_choice])

        # Generate computer choice randomly (0, 1, or 2)
        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(game_images[computer_choice])

        # Game Logic & Rules
        if user_choice == 0 and computer_choice == 2:
            print("You win! 🎉")
        elif computer_choice == 0 and user_choice == 2:
            print("You lose! 😢")
        elif computer_choice > user_choice:
            print("You lose! 😢")
        elif user_choice > computer_choice:
            print("You win! 🎉")
        elif computer_choice == user_choice:
            print("It's a draw! 🤝")

except ValueError:
    print("Invalid input! Please enter a whole number (0, 1, or 2).")
except IndexError:
    print("Index Error! You tried to access an item outside the list range.")