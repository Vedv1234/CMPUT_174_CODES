# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is version 2 of my board game where I'm adding the ability
# to track the game piece's position and count how many times each square is visited.
# I modified my display function to show where the game piece is on the board.

'''VERSION 2 In this version of the game
- write a function called update_position. This function computes the new position of the GAME_PIECE on the board by adding the roll to the previous position. This function also increments the number of times the game piece has visited a square on the board.
- modify the display_board function such that it now displays the game_piece at its current position
'''

import random
GAME_PIECE = '@'

def create_board(size: int) -> list:
    # I'm creating my game board here as a list of zeros
    board = [0] * size
    return board

def display_board(board: list, position: int) -> None:
    # My updated display function now shows both visit counts and the game piece
    display_str = '|'
    for index in range(len(board)):
        if index == position:
            # When I'm at the current position, increment visit count and show the game piece
            board[index] = board[index] + 1
            display_str = f'{display_str}{board[index]}{GAME_PIECE}|'
        else:
            # For other positions, just show the visit count
            display_str = f'{display_str}{board[index]}|'
    print('=' * len(display_str))
    print(display_str)
    print('=' * len(display_str))    

def roll_die(sides: int) -> int:
    # My dice rolling function with a prompt
    input('Press enter to roll ...')
    number = random.randint(1, sides)
    return number

def update_position(board, previous_position, roll):
    # I'm calculating the new position using modulo to wrap around the board
    new_position = (previous_position + roll) % len(board)
    return new_position

def main() -> None:
    # My main game loop with the new position tracking
    current_position = -1
    
    # Getting game setup from player
    size = int(input('Enter size of board > '))
    board = create_board(size)
    display_board(board, current_position)
    
    # Getting die setup and making first move
    sides = int(input('How many sides does the die have?'))
    roll = roll_die(sides)
    print(f'You rolled {roll}.')
    current_position = update_position(board, current_position, roll)
    display_board(board, current_position)
    
main()