# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: In this third version of my dungeon crawler, I've added the ability
# for the player to actually move around the map! This is where the game really starts to 
# come together. I've implemented the movement system that lets players type commands like
# 'go north' to navigate through the dungeon. It's getting more exciting now that players
# can explore the map!

# Still using my constant for the map file
MAP_FILE = 'cave_map.txt'

def load_map(map_file: str) -> list[list[str]]:
    # My trusty map loader hasn't changed
    with open(map_file, 'r') as file:
        return [list(line.strip()) for line in file]

def find_start(grid: list[list[str]]) -> list[int, int]:
    # Still using my start position finder
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                return [i, j]

def get_command() -> str:
    # My command getter remains the same
    return input("Enter a command: ")

def display_map(grid: list[list[str]], player_position: list[int, int]) -> None:
    # My map display function hasn't changed
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if [i, j] == player_position:
                print('@', end='')
            else:
                print(cell, end='')
        print()

def get_grid_size(grid: list[list[str]]) -> list[int, int]:
    # Still using my grid size helper
    return [len(grid), len(grid[0])]

def is_inside_grid(grid: list[list[str]], position: list[int, int]) -> bool:
    # My boundary checker remains the same
    grid_rows, grid_cols = get_grid_size(grid)
    return 0 <= position[0] < grid_rows and 0 <= position[1] < grid_cols

def look_around(grid: list[list[str]], player_position: list[int, int]) -> list:
    # My direction checker hasn't changed
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
        directions.append('east')

    return directions

def move(direction: str, player_position: list[int, int], grid: list[list[str]]) -> bool:
    # This is my new function that handles player movement
    directions = look_around(grid, player_position)

    # I first check if the direction is valid
    if direction.lower() in directions:
        row, col = player_position
        
        # Then I update the player's position based on the direction
        if direction.lower() == 'north':
            player_position[0] = row - 1
        elif direction.lower() == 'south':
            player_position[0] = row + 1
        elif direction.lower() == 'west':
            player_position[1] = col - 1
        elif direction.lower() == 'east':
            player_position[1] = col + 1

        return True
    else:
        return False

def main():
    # Loading my map and finding the start position
    dungeon_map = load_map(MAP_FILE)
    start_position = find_start(dungeon_map)

    while True:
        # Checking available directions at the start of each turn
        directions = look_around(dungeon_map, start_position)

        if directions:
            print(f"You can go {', '.join(directions)}")
        else:
            print("There is no way to go.")

        command = get_command()

        # I've added movement commands to my command handler
        if command.lower() == 'escape':
            print("$ exit")
            break
        elif command.lower() == 'show map':
            display_map(dungeon_map, start_position)
        elif command.lower() in ['go north', 'go south', 'go west', 'go east']:
            # I extract just the direction part from the command
            move_direction = command.lower().split()[1]
            if move(move_direction, start_position, dungeon_map):
                print(f"You moved {move_direction}.")
            else:
                print("There is no way there.")
        else:
            print("I do not understand. Please enter a valid command.")

if __name__ == '__main__':
    main()