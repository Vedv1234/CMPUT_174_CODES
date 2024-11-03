# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: In this version of my SimCity project, I've added the ability to fill in
# missing land values. I'm using the neighbor values I found earlier to calculate reasonable values
# for any empty spots in my grid. This is where the simulation really comes together, as I can now
# complete incomplete land value data by looking at surrounding values.

# I need deepcopy to make sure I don't accidentally change my original grid
from copy import deepcopy

def find_neighbor_values(grid: list[list[int]], row: int, col: int) -> list[int]:
    """
    Find the neighbors of a cell
    """
    # First I need to know how big my grid is
    num_rows = len(grid)
    num_cols = len(grid[0])

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
        if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
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
        print(" ".join(f"{value:>{9}}" for value in row))

def fill_gaps(grid: list[list[int]]) -> list[list[int]]:
    """
    Fill the gaps in the grid
    """
    # I need to make a complete copy of my grid so I don't mess with the original
    new_grid = deepcopy(grid)

    # Time to go through every single cell in my grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # If I find a missing value (marked as 0), I need to fill it
            if grid[row][col] == 0:
                # First, I get all the neighbor values for this spot
                neighbors = find_neighbor_values(grid, row, col)
                # Then I calculate the average of all neighbors and round it
                average_value = round(sum(neighbors) / len(neighbors))
                # Finally, I can fill in the missing spot with my calculated value
                new_grid[row][col] = average_value

    return new_grid

def main() -> None:
    """
    Main program.
    """
    # First, I need to load my grid from the data file
    grid = create_grid("data_0.txt")
    # I'll add a nice header to make it clear what I'm showing
    print("SimCity land values:")
    # Show the original grid first
    display_grid(grid)
    # Now I'll show the grid with all the gaps filled in
    print("\nCalculated SimCity land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)

# This is where my program starts running
if __name__ == "__main__":
    main()