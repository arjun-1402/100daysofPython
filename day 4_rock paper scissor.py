import random

# ASCII Art for the game
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

# Game options list
game_images = [rock, paper, scissors]

# User choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))

if user_choice >= 3 or user_choice < 0:
    print("Invalid choice! You lose.")
else:
    print(game_images[user_choice])

    # Computer choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 1 and computer_choice == 0:
        print("You win!")
    elif user_choice == 2 and computer_choice == 1:
        print("You win!")
    else:
        print("You lose!")
