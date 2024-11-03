# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: In this part of my SimCity project, I've created functions to read and display
# a grid of land values from a file. I'm basically setting up the foundation for the whole simulation
# by handling the basic grid operations. This is where I load the initial land values and figure out
# how to show them nicely on screen.

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