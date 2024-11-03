# Author: Ved Vyas
# Functionality of code: This is my test suite for the gap-filling functionality in my SimCity project.
# I've created tests to make sure my function correctly calculates missing values by averaging
# neighboring cells. Each test checks a different position in the grid to ensure my calculations
# work properly everywhere.

"""
Unit tests for the fill_gaps() function

Using the following grid:
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16
"""

# Importing the function I want to test
from simcity3 import fill_gaps
# I need deepcopy to make copies of my test grid
from copy import deepcopy

def avg_rounded(values):
    """My helper function to calculate the average and round it"""
    return round(sum(values) / len(values))

# Setting up my test grid with simple numbers that make it easy to verify calculations
GRID = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

def test_fill_gaps_top_left_corner():
    """
    Corner cell (top left)
    Neighbors of 1 should be 2, 5, 6 (in any order)
    """
    # I make a fresh copy of my grid for each test
    initial_grid = deepcopy(GRID)
    # Set the top-left corner to 0 (missing value)
    initial_grid[0][0] = 0
    # Fill in the gaps
    new_grid = fill_gaps(initial_grid)
    # Check if the calculated value matches what I expect
    assert new_grid[0][0] == avg_rounded([2, 5, 6])

def test_fill_gaps_top_right_corner():
    """
    Corner cell (top right)
    Neighbors of 4 should be 3, 7, 8 (in any order)
    """
    # Make a fresh copy of my test grid
    initial_grid = deepcopy(GRID)
    # Set the top-right corner to 0
    initial_grid[0][3] = 0
    # Fill the gaps
    new_grid = fill_gaps(initial_grid)
    # Verify the calculation
    assert new_grid[0][3] == avg_rounded([3, 7, 8])

def test_fill_gaps_bottom_left_corner():
    """
    Corner cells (bottom left)
    Neighbors of 13 should be 9, 10, 14 (in any order)
    """
    # Create another fresh grid copy
    initial_grid = deepcopy(GRID)
    # Set bottom-left corner to 0
    initial_grid[3][0] = 0
    # Fill the gaps
    new_grid = fill_gaps(initial_grid)
    # Check the result
    assert new_grid[3][0] == avg_rounded([9, 10, 14])

def test_fill_gaps_bottom_right_corner():
    """
    Corner cells (bottom right)
    Neighbors of 16 should be 11, 12, 15 (in any order)
    """
    # New grid copy for this test
    initial_grid = deepcopy(GRID)
    # Set bottom-right corner to 0
    initial_grid[3][3] = 0
    # Fill gaps
    new_grid = fill_gaps(initial_grid)
    # Verify the result
    assert new_grid[3][3] == avg_rounded([11, 12, 15])

def test_fill_gaps_left_edge():
    """
    Edge cell (left edge)
    Neighbors of 5 should be 1, 2, 6, 9, 10 (in any order)
    """
    # Fresh grid copy
    initial_grid = deepcopy(GRID)
    # Set left edge cell to 0
    initial_grid[1][0] = 0
    # Fill gaps
    new_grid = fill_gaps(initial_grid)
    # Check the calculation
    assert new_grid[1][0] == avg_rounded([1, 2, 6, 9, 10])

def test_fill_gaps_top_edge():
    """
    Edge cell (top edge)
    Neighbors of 2 should be 1, 3, 5, 6, 7 (in any order)
    """
    # New grid copy
    initial_grid = deepcopy(GRID)
    # Set top edge cell to 0
    initial_grid[0][1] = 0
    # Fill gaps
    new_grid = fill_gaps(initial_grid)
    # Verify result
    assert new_grid[0][1] == avg_rounded([1, 3, 5, 6, 7])

def test_fill_gaps_right_edge():
    """
    Edge cell (right edge)
    Neighbors of 8 should be 3, 4, 7, 11, 12 (in any order)
    """
    # Fresh grid copy
    initial_grid = deepcopy(GRID)
    # Set right edge cell to 0
    initial_grid[1][3] = 0
    # Fill gaps
    new_grid = fill_gaps(initial_grid)
    # Check calculation
    assert new_grid[1][3] == avg_rounded([3, 4, 7, 11, 12])

def test_fill_gaps_bottom_edge():
    """
    Edge cell (bottom edge)
    Neighbors of 15 should be 10, 11, 12, 14, 16 (in any order)
    """
    # Last grid copy
    initial_grid = deepcopy(GRID)
    # Set bottom edge cell to 0
    initial_grid[3][2] = 0
    # Fill gaps
    new_grid = fill_gaps(initial_grid)
    # Verify final calculation
    assert new_grid[3][2] == avg_rounded([10, 11, 12, 14, 16])