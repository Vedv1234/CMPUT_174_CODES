# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my Pac-Boy game where I created a board game with
# a player character (👦) who needs to eat melons (🍉) while avoiding ghosts (👻).
# I'm using emojis and 2D lists to make it more interesting!

import random

# My game constants
BOARD_SIZE = 5
PAC_BOY = '👦'
MELON = '🍉'
GHOST = '👻'
EMPTY = '🔹'
NUMBER_OF_GHOSTS = 3
NUMBER_OF_MELONS = 5

def create_board():
    # I'm creating my empty game board as a 2D list
    board = []
    for row_index in range(BOARD_SIZE):
        a_row = []
        for col_index in range(BOARD_SIZE):
            a_row.append(EMPTY)
        board.append(a_row)
    return board

def display_board(board, melons_eaten):
    # This is my function to show the current game state
    for row in board:
        string = '|'
        for col in row:
            string = f'{string}{col}|'  # Making each row look nice with borders
        print(string)
    print(f'Melons Eaten : {melons_eaten}')

def initialize_board(board, items, location):
    # I'm setting up my board with Pac-Boy, ghosts, and melons
    row = location[0]
    col = location[1]
    board[row][col] = PAC_BOY
    # Placing each item (ghosts and melons) randomly
    for item in items:
        placed = False
        while not placed:
            random_row = random.randint(0, BOARD_SIZE - 1)
            random_col = random.randint(0, BOARD_SIZE - 1)
            if board[random_row][random_col] == EMPTY:
                board[random_row][random_col] = item
                placed = True

def update_location(move, location):
    # My function to move Pac-Boy based on user input
    row = location[0]
    col = location[1]
    updated = False
    # Checking each direction and making sure we stay on the board
    if move == 'S' and row + 1 < BOARD_SIZE:
        row = row + 1
        updated = True
    elif move == 'N' and row - 1 >= 0:
        row = row - 1
        updated = True
    elif move == 'E' and col + 1 < BOARD_SIZE:
        col = col + 1
        updated = True
    elif move == 'W' and col - 1 >= 0:
        col = col - 1
        updated = True
    
    if updated:
        location[0] = row
        location[1] = col
    else:
        print('Move Invalid')
    return updated

def check_content(board: list, location: list, melons_eaten: int):
    # I'm checking what Pac-Boy ran into
    continue_game = True
    row = location[0]
    col = location[1]
    if board[row][col] == GHOST:
        continue_game = False  # Game over if we hit a ghost
    elif board[row][col] == MELON:
        melons_eaten = melons_eaten + 1
        if melons_eaten == NUMBER_OF_MELONS:
            continue_game = False  # Win if we get all melons
    return continue_game, melons_eaten

def update_board(board: list, old_location: list, new_location: list):
    # My function to update the board after Pac-Boy moves
    # First clear the old position, then show Pac-Boy in new position
    board[old_location[0]][old_location[1]] = EMPTY
    board[new_location[0]][new_location[1]] = PAC_BOY

def display_outcome(melons_eaten):
    # I'm showing different messages based on how the game ended
    if melons_eaten == NUMBER_OF_MELONS:
        print('You win the game !!!!')  # Victory message
    else:
        print('Boo! A ghost scared you !!!')  # Game over message

def main():
    # This is my main game loop where everything comes together
    
    # Initial game setup
    board = create_board()
    melons_eaten = 0
    display_board(board, melons_eaten)
    
    # Setting up Pac-Boy's starting position and game items
    location = [0, 0]
    # I'm creating a list with the right number of ghosts and melons
    items = [GHOST] * NUMBER_OF_GHOSTS + [MELON] * NUMBER_OF_MELONS
    initialize_board(board, items, location)
    display_board(board, melons_eaten)
    
    # My main game loop
    continue_game = True
    while continue_game:
        # Getting player's move
        move = input('Enter N,S,E,W:').upper()
        old_location = location[:]  # Making a copy of current location
        
        # Updating game state if move is valid
        updated = update_location(move, location)
        if updated:
            continue_game, melons_eaten = check_content(board, location, melons_eaten)
            update_board(board, old_location, location)
            display_board(board, melons_eaten)
    
    # Show final result
    display_outcome(melons_eaten)

# Making sure the game only runs if this file is run directly
if __name__ == '__main__':
    main()