# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is version 3 of my board game where I've added win/lose 
# conditions. The game ends if a player visits all squares at least once (win) or 
# visits the same square too many times (lose). I've added a game loop to keep playing
# until one of these conditions is met.

'''VERSION 3 In this version of the game
- add a function called is_game_over. This function returns True if a space in the board has been visited MAX_VISITS times or if all spaces in the board have been visited at least once.
- modify the main function such that the roll_die, update_board and display_board are called until the game is over.
- add a function called display_result.  This function displays "Congratulations, you won." message if the player is able to move the game piece to each square of the board at least once. It displays"Unfortunately, you lost." message if the game piece is moved to a square MAX_VISITS times. 
'''

import random
GAME_PIECE = '@'
MAX_VISITS = 3

def is_game_over(board):
    # I check two conditions here:
    # 1. If any square has been visited MAX_VISITS times (lose condition)
    # 2. If all squares have been visited at least once (win condition)
    if MAX_VISITS in board or 0 not in board:
        return True
    else:
        return False

def create_board(size: int) -> list:
    # Creating my initial board with zeros
    board = [0] * size
    return board

def display_board(board: list, position: int) -> None:
    # My display function showing visit counts and game piece
    display_str = '|'
    for index in range(len(board)):
        if index == position:
            board[index] = board[index] + 1
            display_str = f'{display_str}{board[index]}{GAME_PIECE}|'
        else:
            display_str = f'{display_str}{board[index]}|'
    print('=' * len(display_str))
    print(display_str)
    print('=' * len(display_str))    

def roll_die(sides: int) -> int:
    # My dice rolling function
    input('Press enter to roll ...')
    number = random.randint(1, sides)
    return number

def update_position(board, previous_position, roll):
    # Calculating new position with wraparound using modulo
    new_position = (previous_position + roll) % len(board)
    return new_position

def display_result(board):
    # I check which end condition was met and show the appropriate message
    if MAX_VISITS in board:
        print('You lose !')
    else:
        print('You win !')

def main() -> None:
    # My main game loop now runs until a win/lose condition is met
    current_position = -1
    
    # Getting initial setup from player
    size = int(input('Enter size of board > '))
    board = create_board(size)
    display_board(board, current_position)
    sides = int(input('How many sides does the die have?'))
    
    # Main game loop
    game_over = is_game_over(board)
    while not game_over:
        roll = roll_die(sides)
        print(f'You rolled {roll}.')
        current_position = update_position(board, current_position, roll)
        display_board(board, current_position)
        game_over = is_game_over(board)
    
    # Show final result
    display_result(board)
    
main()