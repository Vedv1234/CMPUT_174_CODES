# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: In this second version of my dungeon crawler, I've added some cool 
# new features like map display and the ability to look around. I've made the game more 
# interactive by showing the player's position with an '@' symbol and letting them see 
# which directions they can move in. This version makes the game feel more like a real 
# dungeon crawler!

# I'm keeping my map file constant from the first version
MAP_FILE = 'cave_map.txt'

def load_map(map_file: str) -> list[list[str]]:
    # This is my map loading function from before
    with open(map_file, 'r') as file:
        return [list(line.strip()) for line in file]

def find_start(grid: list[list[str]]) -> list[int, int]:
    # Still using my start position finder from the first version
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                return [i, j]

def get_command() -> str:
    # My simple command getter hasn't changed
    return input("Enter a command: ")

def display_map(grid: list[list[str]], player_position: list[int, int]) -> None:
    # This is my new function to show the map with the player's position
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            # I'm using '@' to show where the player is on the map
            if [i, j] == player_position:
                print('@', end='')
            else:
                # For all other positions, I just show the map character
                print(cell, end='')
        # After each row, I need a new line
        print()

def get_grid_size(grid: list[list[str]]) -> list[int, int]:
    # I made this helper function to easily get my map dimensions
    return [len(grid), len(grid[0])]

def is_inside_grid(grid: list[list[str]], position: list[int, int]) -> bool:
    # This helps me check if a position is actually on my map
    grid_rows, grid_cols = get_grid_size(grid)
    return 0 <= position[0] < grid_rows and 0 <= position[1] < grid_cols

def look_around(grid: list[list[str]], player_position: list[int, int]) -> list:
    # This is where I check what directions the player can move
    # I'm defining what objects the player can move onto
    allowed_objects = ('S', 'F', '*')
    directions = []
    row, col = player_position

    # I check each direction (north, south, west, east) to see if it's a valid move
    if is_inside_grid(grid, [row - 1, col]) and grid[row - 1][col] in allowed_objects:
        directions.append('north')
    if is_inside_grid(grid, [row + 1, col]) and grid[row + 1][col] in allowed_objects:
        directions.append('south')
    if is_inside_grid(grid, [row, col - 1]) and grid[row][col - 1] in allowed_objects:
        directions.append('west')
    if is_inside_grid(grid, [row, col + 1]) and grid[row][col + 1] in allowed_objects:
        directions.append('east')

    return directions

def main():
    # Loading my map and finding the start position
    dungeon_map = load_map(MAP_FILE)
    start_position = find_start(dungeon_map)

    while True:
        # Now I'm checking what directions are available before each turn
        directions = look_around(dungeon_map, start_position)
        
        # I tell the player what directions they can move in
        if directions:
            print(f"You can go {', '.join(directions)}")
        else:
            print("There is no way to go.")
            
        command = get_command()

        # I've added the 'show map' command to my game
        if command.lower() == 'escape':
            print("$ exit")
            break
        elif command.lower() == 'show map':
            display_map(dungeon_map, start_position)
        else:
            print("I do not understand. Please enter a valid command.")

if __name__ == '__main__':
    main()