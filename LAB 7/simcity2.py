# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is where I've added the neighbor-finding functionality to my SimCity project.
# I needed a way to look at all the surrounding land values for any given cell in my grid. This is super
# important because later I'll use these values to calculate missing land values. I kept all the grid
# creation and display stuff from before, but added this new neighbor-finding feature.

def find_neighbor_values(grid: list[list[int]], row: int, col: int) -> list[int]:
    """
    Find the neighbors of a cell
    """
    # Starting with an empty list to store all the neighbor values I find
    neighbors = []

    # These are all the possible directions I need to check for neighbors
    # Each tuple represents a direction: (row_change, column_change)
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # Now I'll check each direction for valid neighbors
    for offset_row, offset_col in offsets:
        # Calculate where this neighbor would be
        new_row = row + offset_row
        new_col = col + offset_col

        # I need to make sure I don't go outside my grid boundaries
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            # If it's valid, I'll add this neighbor's value to my list
            neighbors.append(grid[new_row][new_col])

    return neighbors

def create_grid(filename: str) -> list[list[int]]:
    """
    Create a grid of land values from a file
    """
    # I start with an empty list that will eventually hold all my grid values
    grid = []

    # Here I'm opening my data file - I made sure to use 'with' for proper file handling
    with open(filename, 'r') as file:
        # First I need to get all the lines from my file
        lines = file.readlines()

        # The first two lines are special - they tell me the grid size
        # I'm grabbing the number of rows first
        num_rows = int(lines[0].strip())
        lines.pop(0)  # Get rid of that line since I'm done with it
        # Now I get the number of columns
        num_cols = int(lines[0].strip())
        lines.pop(0)  # And remove this line too
        
        # Time to build my actual grid with the land values
        grid = []  # Fresh start for my grid
        c = 0  # I'll use this to keep track of which line I'm reading
        for i in range(num_rows):  # Going through each row
            grid.append([])  # Adding a new row to my grid
            for j in range(num_cols):  # Fill in each column in this row
                grid[i].append(int(lines[c]))  # Convert the text to a number and add it
                c += 1  # Move to the next line in my file

    # All done! Now I can return my completed grid
    return grid

def display_grid(grid: list[list[int]]) -> None:
    """
    Display a grid of land values
    """
    # I'm going through each row in my grid to display it
    for row in grid:
        a_row = []  # This will hold the formatted values for one row
        for col in row:  # Going through each value in the current row
            a_row += str(col)  # Convert the number to text and add it
        
        # I want my numbers to look nice and aligned, so I'm using right-justified formatting
        # Each value gets 9 spaces, making it look clean and organized
        print(" ".join(f"{value:>{9}}" for value in row))

def main() -> None:
    """
    Main program.
    """
    # First, I need to load my grid from the data file
    grid = create_grid("data_0.txt")
    # I'll add a nice header to make it clear what I'm showing
    print("SimCity Land Values:")
    # Now I can show my grid in a nice formatted way
    display_grid(grid)

# This is where my program starts running
if __name__ == "__main__":
    main()