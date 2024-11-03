# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my first version of a dungeon crawler game that I created 
# for Lab 8. In this initial version, I focused on setting up the basic structure of the game
# by implementing map loading, finding the starting position, and handling basic user commands.
# It's pretty simple right now but sets up the foundation for more complex features I'll add later.

# I'm defining a constant for my map file name that I'll use throughout the code
MAP_FILE = 'cave_map.txt'

def load_map(map_file: str) -> list[list[str]]:
    # I'm creating a function to load my map from a file
    # It takes a file path and returns a 2D list representing the map
    with open(map_file, 'r') as file:
        # Here I'm reading each line, removing whitespace, and converting it to a list of characters
        # This creates my 2D grid structure for the map
        return [list(line.strip()) for line in file]

def find_start(grid: list[list[str]]) -> list[int, int]:
    # I need to find where the player starts on the map
    # I'm searching through my grid to find the 'S' character
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                # When I find the 'S', I return its position as [row, column]
                return [i, j]

def get_command() -> str:
    # This is my simple function to get user input
    # I'm just asking the player what they want to do
    return input("Enter a command: ")

def main():
    # First, I need to load my dungeon map
    dungeon_map = load_map(MAP_FILE)
    
    # I want to show the player what the map looks like
    print("Loaded Map:")
    for row in dungeon_map:
        # I'm printing each row of the map by joining all its characters
        print(''.join(row))
    
    # Now I need to find where the player starts
    start_position = find_start(dungeon_map)
    print(f"Starting Position: {start_position}")
    
    # This is my main game loop where I handle player commands
    while True:
        command = get_command()
        # I'm checking if the player wants to quit
        if command.lower() == 'escape':
            print(" $ exit")
            break
        else:
            # If I don't recognize the command, I let the player know
            print("I do not understand. Please enter a valid command.")

if __name__ == '__main__':
    main()