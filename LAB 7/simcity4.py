# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is the final version of my SimCity project where I've added some
# statistical analysis. Now I can find both the maximum and average land values in my city grid.
# This helps me understand the overall land value distribution and identify the most valuable
# areas in my simulated city.

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
        c = 0  # I'll use this to keep track