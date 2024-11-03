# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is version 1 of my board game project where I'm setting up 
# the basic structure. I created functions to make a game board, display it, and 
# implement dice rolling. It's my first step in building a more complex board game.

'''VERSION 1 In this version of the game 
- create a game piece
- initialize the position of the game piece to NOT ON BOARD
- prompt the user to enter the size of the board.
- prompt the user to enter the number of sides of a die
- write a function called create_board that takes in the board_size as an argument and creates and initializes the board.
- write a function that displays the initialized board. For example, if board size is 5, a call to display_board should display:
===========
|0|0|0|0|0|
===========
- write a function called roll_die that takes in the number of sides as an arguments and returns the value of a roll
'''

import random

def create_board(size: int) -> list:
    # I'm creating my game board here by making a list filled with zeros
    # The size parameter tells me how long to make the board
    board = [0] * size
    return board

def display_board(board: list) -> None:
    # This is my function to show the board nicely formatted with borders
    # I'm building a string with pipe separators between each cell
    display_str = '|'
    for index in range(len(board)):
        display_str = f'{display_str}{board[index]}|'
    # I'm adding equal signs on top and bottom to make it look like a proper board
    print('=' * len(display_str))
    print(display_str)
    print('=' * len(display_str))    

def roll_die(sides: int) -> int:
    # My dice rolling function - it waits for the player to press enter
    # then gives a random number between 1 and the number of sides
    input('Press enter to roll ..')
    number = random.randint(1, sides)
    return number
    
def main() -> None:
    # This is where I set up my game and test my functions
    # Setting up initial game variables
    game_piece = '@'
    current_position = -1  # I'm using -1 to show the piece isn't on the board yet
    
    # Getting board setup from the player
    size = int(input('Enter size of board > '))
    board = create_board(size)
    display_board(board)
    
    # Getting die setup and doing first roll
    sides = int(input('How many sides does your die have ?'))
    roll = roll_die(sides)
    print(f'You rolled {roll}.')

main()