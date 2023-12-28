# My Second Game in Python : Rock, Paper, Scissors

import random          # Importing the random module
import sys             # Importing the sys module

# Game Assets
game_assets = ['rock', 'paper', 'scissors']

# Randomly pick an item from the list
random_choice = random.choice(game_assets)
#print(random_choice)           # Game Testing
print('\n')
user_input = input('Pick one of these elements: Rock, Paper, Scissors: ')

# Exit the Game
if user_input == 'q':
    sys.exit()


def game():
    """This Function Should have the game work."""

    # Implementing the game tie conditions
    if user_input.lower() == 'rock' and random_choice == 'rock':
        print(f'The A.I has chosen {random_choice.title()}, while you have chosen {user_input.title()}.')
        print('This is a tie.')
    elif user_input.lower() == 'paper' and random_choice == 'paper':
        print(f'The A.I has chosen {random_choice.title()}, while you have chosen {user_input.title()}.')
        print('This is a tie.')
    elif user_input.lower() == 'scissors' and random_choice == 'scissors':
        print(f'The A.I has chosen {random_choice.title()}, while you have chosen {user_input.title()}.')
        print('This is a tie.')

    # Implementing the game 'rock' conditions
    if user_input.lower() == 'rock' and random_choice == 'paper':
        print(f'The A.I has chosen {random_choice.title()}, while you have chosen {user_input.title()}.')
        print('You have lost.')
    elif user_input.lower() == 'rock' and random_choice == 'scissors':
        print(f'The A.I has chosen {random_choice.title()}, while you have chosen {user_input.title()}.')
        print('You have won!.')

    # Implementing the game 'paper' conditions
    if user_input.lower() == 'paper' and random_choice == 'rock':
        print(f'The A.I has chosen {random_choice.title()}, while you have chosen {user_input.title()}.')
        print('You have won!')
    elif user_input.lower() == 'paper' and random_choice == 'scissors':
        print(f'The A.I has chosen {random_choice.title()}, while you have chosen {user_input.title()}.')
        print('You have lost.')

    # Implementing the game 'scissors' conditions
    if user_input.lower() == 'scissors' and random_choice == 'rock':
        print(f'The A.I has chosen {random_choice.title()}, while you have chosen {user_input.title()}.')
        print('You have lost!')
    elif user_input.lower() == 'scissors' and random_choice == 'paper':
        print(f'The A.I has chosen {random_choice.title()}, while you have chosen {user_input.title()}.')
        print('You have won.')

    sys.exit()



game()
