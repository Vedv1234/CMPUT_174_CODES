# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my board game with win/lose conditions. Players win by
# visiting all squares at least once and lose if they visit the same square too many
# times. I've added a game loop and result display to make it more interactive.

'''[Original version description kept for reference]'''

import random
GAME_PIECE = '@'
MAX_VISITS = 3

def is_game_over(board):
    # I'm checking two conditions to end the game:
    # 1. If a square is visited too many times (lose)
    # 2. If all squares are visited at least once (win)
    if MAX_VISITS in board or 0 not in board:
        return True
    else:
        return False

def create_board(size: int) -> list:
    # I'm creating my game board with all zeros to track visits
    board = [0] * size
    return board

def display_board(board: list, position: int) -> None:
    # This is my display function that shows the current state of the board
    display_str = '|'
    for index in range(len(board)):
        if index == position:
            # When I'm at the current position, increment visits and show the game piece
            board[index] = board[index] + 1
            display_str = f'{display_str}{board[index]}{GAME_PIECE}|'
        else:
            # For other positions, just show the visit count
            display_str = f'{display_str}{board[index]}|'
    # Adding borders to make it look nice
    print('=' * len(display_str))
    print(display_str)
    print('=' * len(display_str))    

def roll_die(sides: int) -> int:
    # My dice rolling function with user interaction
    input('Press enter to roll ...')
    number = random.randint(1, sides)
    return number

def update_position(board, previous_position, roll):
    # I'm calculating the new position using modulo to wrap around the board
    new_position = (previous_position + roll) % len(board)
    return new_position

def display_result(board):
    # I show different messages based on how the game ended
    if MAX_VISITS in board:
        print('You lose !')
    else:
        print('You win !')

def main() -> None:
    # This is my main game loop where everything comes together
    current_position = -1  # Starting off the board
    
    # Getting game setup from the player
    size = int(input('Enter size of board > '))
    board = create_board(size)
    display_board(board, current_position)
    sides = int(input('How many sides does the die have?'))
    
    # My main game loop that runs until win/lose condition
    game_over = is_game_over(board)
    while not game_over:
        roll = roll_die(sides)
        print(f'You rolled {roll}.')
        current_position = update_position(board, current_position, roll)
        display_board(board, current_position)
        game_over = is_game_over(board)
    
    # Showing final result
    display_result(board)
    
main()