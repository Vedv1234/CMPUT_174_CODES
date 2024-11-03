# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This looks like my initial attempt at the board game where
# I set up the basic structure. It's similar to board1 but with a different display
# character (⧆) and slightly different formatting. I kept this version as a backup
# while developing the more advanced versions.

import random

def create_board(size):
    # Creating my initial board with zeros
    board = [0] * int(size)
    return board

def display_board(board, board_size):
    # My basic board display function with borders
    display_str = '|'
    for index in range(board_size):
        display_str = f"{display_str}{board[index]}|"
    print('=' * len(display_str))
    print(display_str)
    print('=' * len(display_str))
    
def roll_die(sides):
    # My dice rolling function
    input(' Press enter to roll....')
    roll = random.randint(1, sides)
    return roll

def main():
    # Setting up my game variables
    game_piece = '⧆'
    current_position = -1  # not on the board
    
    # Getting board setup from player
    board_size = int(input("enter board size>"))
    board = create_board(board_size)
    display_board(board, board_size)
    
    # Getting die setup and doing first roll
    sides = int(input(' Enter sides >'))
    roll_die(sides)
    roll = roll_die(sides)
    print(f' you rolled {roll}')

main()