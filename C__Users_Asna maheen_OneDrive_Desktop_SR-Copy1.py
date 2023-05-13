#!/usr/bin/env python
# coding: utf-8

# # ROCK PAPER SCISSOR GAME(BASIC)
# 

# In[7]:


import random

# Define a list of options for the game
options = ['rock', 'paper', 'scissors']

# Define a function that runs the game
def play_game():
    # Prompt the user to choose an option
    user_choice = input('Choose rock, paper, or scissors: ').lower()
    # Generate a random option for the computer
    computer_choice = random.choice(options)
    # Print the user's and computer's choices
    print(f'You chose {user_choice}.')
    print(f'The computer chose {computer_choice}.')
    # Determine the winner of the game
    if user_choice == computer_choice:
        print('The game is a tie!')
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print('You win!')
    elif user_choice == 'paper' and computer_choice == 'rock':
        print('You win!')
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print('You win!')
    else:
        print('The computer wins!')

# Run the game
play_game()


# In[ ]:




