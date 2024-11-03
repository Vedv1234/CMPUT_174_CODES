# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my second version of the board game where I've added
# position tracking and a cool diamond (⧆) game piece. I'm using this to learn about
# game state management and how to update positions on a board.

import random
game_piece = '⧆'  # I'm using this diamond symbol as my game piece constant

def update_board(board, previous_position, roll):
    # I'm calculating the new position by using modulo to wrap around the board
    # when the piece reaches the end
    new_position = (previous_position + roll) % len(board)
    return new_position

def create_board(size):
    # I'm creating my game board as a list of zeros, converting size to int just to be safe
    board = [0] * int(size)
    return board

def display_board(board: list, position: int):
    # This is my function to show the board with visit counts
    display_str = '|'
    for index in range(len(board)):
        if index == position:
            # When I'm at the current position, I increment the visit counter
            board[index] = board[index] + 1
            display_str = (f"{display_str}{board[index]}|")
        else:
            # For other positions, just show their current count
            display_str = (f"{display_str}{board[index]}|")
    # I'm adding borders to make it look nice
    print('=' * len(display_str))
    print(display_str)
    print('=' * len(display_str))
    
def roll_die(sides):
    # My dice rolling function that waits for player input
    input(' Press enter to roll....')
    roll = random.randint(1, sides)
    return roll

def main():
    # My main game function where everything comes together
    current_position = -1  # I start with -1 to show the piece isn't on the board yet
    
    # Getting the board size from the player
    board_size = int(input("enter board size>"))
    board = create_board(board_size)
    display_board(board, current_position)
    
    # Setting up the die and doing the first roll
    sides = int(input(' Enter sides >'))
    roll_die(sides)
    roll = roll_die(sides)
    print(f' you rolled {roll}')
    
    # Updating and showing the new board state
    current_position = update_board(board, current_position, roll)
    display_board(board, current_position)

main()