# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my third version of the board game where I've added
# win/lose conditions and a game loop. Players can now win by visiting all squares
# at least once, or lose by visiting the same square too many times.

import random
game_piece = '⧆'  # I'm using this diamond as my game piece
max_visits = 3    # I'll use this to limit how many times a square can be visited

def update_board(board, previous_position, roll):
    # My function to calculate the new position with wraparound
    new_position = (previous_position + roll) % len(board)
    return new_position

def is_game_over(board):
    # I'm checking two conditions for game over:
    # 1. If any square is visited max times (lose)
    # 2. If all squares are visited at least once (win)
    if max_visits in board or 0 not in board:
        return True
    else:
        return False

def display_result(board: list):
    # I show different messages depending on how the game ended
    if max_visits in board:
        print(" You lose, not your day")
    else:
        print("You win! Congrats")

def create_board(size):
    # Creating my initial board with all zeros
    board = [0] * int(size)
    return board

def display_board(board: list, position: int):
    # My improved display function now shows both the game piece and visit counts
    display_str = '|'
    for index in range(len(board)):
        if index == position:
            board[index] = board[index] + 1
            display_str = (f"{display_str}{game_piece}{board[index]}|")
        else:
            display_str = (f"{display_str}{board[index]}|")
    print('=' * len(display_str))
    print(display_str)
    print('=' * len(display_str))
    
def roll_die(sides):
    # My dice rolling function with player input
    input(' Press enter to roll....')
    roll = random.randint(1, sides)
    return roll

def main():
    # My main game loop with win/lose conditions
    current_position = -1  # Starting off the board
    
    # Getting initial setup from player
    board_size = int(input("enter board size>"))
    board = create_board(board_size)
    display_board(board, current_position)
    sides = int(input(' Enter sides >'))
    
    # My game loop that runs until win or lose condition is met
    game_over = is_game_over(board)
    while not game_over:
        roll = roll_die(sides)
        print(f' you rolled {roll}')
        current_position = update_board(board, current_position, roll)
        display_board(board, current_position)
        game_over = is_game_over(board)
    
    # Showing the final result
    display_result(board)

main()