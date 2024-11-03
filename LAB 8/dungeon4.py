# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is the final version of my dungeon crawler game, and it's
# the most exciting one! I've added cool emojis to make the map look better, included
# a help system, and added a victory condition when reaching the finish point. I've also
# made the code more organized by splitting up the game loop into smaller functions.
# This version really brings everything together into a complete game!

# I'm adding a new constant for my help file alongside my map file
MAP_FILE = 'cave_map.txt'
HELP_FILE = 'help.txt'

def load_map(map_file: str) -> list[list[str]]:
    # My map loader remains the same
    with open(map_file, 'r') as file:
        return [list(line.strip()) for line in file]

def find_start(grid: list[list[str]]) -> list[int, int]:
    # Still using my start position finder
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                return [i, j]

def get_command() -> str:
    # My command getter hasn't changed
    return input("Enter a command: ")

def display_map(grid: list[list[str]], player_position: list[int, int]) -> None:
    # I've updated my map display to use cool emojis!
    emojis = {"-": "🧱", "S": "🏠", "F": "🏺", "*": "🟢", "@": "🧝"}
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if [i, j] == player_position:
                print(emojis["@"], end='')
            else:
                print(emojis.get(cell, cell), end='')
        print()

def get_grid_size(grid: list[list[str]]) -> list[int, int]:
    # My grid size helper remains the same
    return [len(grid), len(grid[0])]

def is_inside_grid(grid: list[list[str]], position: list[int, int]) -> bool:
    # My boundary checker hasn't changed
    grid_rows, grid_cols = get_grid_size(grid)
    return 0 <= position[0] < grid_rows and 0 <= position[1] < grid_cols

def look_around(grid: list[list[str]], player_position: list[int, int]) -> list:
    # My direction checker remains the same
    allowed_objects = ('S', 'F', '*')
    directions = []
    row, col = player_position

    if is_inside_grid(grid, [row - 1, col]) and grid[row - 1][col] in allowed_objects:
        directions.append('north')
    if is_inside_grid(grid, [row + 1, col]) and grid[row + 1][col] in allowed_objects:
        directions.append('south')
    if is_inside_grid(grid, [row, col - 1]) and grid[row][col - 1] in allowed_objects:
        directions.append('west')
    if is_inside_grid(grid, [row, col + 1]) and grid[row][col + 1] in allowed_objects:
        directions.