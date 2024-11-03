# Author: Ved Vyas
# Functionality of code: This is my test suite for the neighbor-finding function in my SimCity project.
# I've created a set of test cases to make sure my function correctly identifies neighboring cells
# in all possible scenarios - corners, edges, and middle cells. I'm using pytest to verify that
# everything works exactly as expected.

"""
Unit tests for the find_neighbor_values() function

Using the following grid:
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16
"""
# I need pytest for my testing framework
import pytest
# Importing the function I want to test
from simcity2 import find_neighbor_values

# I'm setting up a test grid with simple numbers that make it easy to track neighbors
GRID = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

def test_find_neighbor_values_top_left_corner():
    """
    Corner cell (top left)
    Neighbors of 1 should be 2, 5, 6 (in any order)
    """
    # I'm testing the top-left corner (value 1) which should have exactly 3 neighbors
    assert len(find_neighbor_values(GRID, 0, 0)) == len([2, 5, 6])
    # Making sure I get exactly the right neighbors (2, 5, and 6)
    assert set(find_neighbor_values(GRID, 0, 0)) == set([2, 5, 6])

def test_find_neighbor_values_top_right_corner():
    """
    Corner cell (top right)
    Neighbors of 4 should be 3, 7, 8 (in any order)
    """
    # For the top-right corner (value 4), checking it has 3 neighbors
    assert len(find_neighbor_values(GRID, 0, 3)) == len([3, 7, 8])
    # Verifying I get the correct neighbors (3, 7, and 8)
    assert set(find_neighbor_values(GRID, 0, 3)) == set([3, 7, 8])

def test_find_neighbor_values_bottom_left_corner():
    """
    Corner cells (bottom left)
    Neighbors of 13 should be 9, 10, 14 (in any order)
    """
    # Testing the bottom-left corner (value 13)
    assert len(find_neighbor_values(GRID, 3, 0)) == len([9, 10, 14])
    # Making sure I get the right neighbors (9, 10, and 14)
    assert set(find_neighbor_values(GRID, 3, 0)) == set([9, 10, 14])

def test_find_neighbor_values_bottom_right_corner():
    """
    Corner cells (bottom right)
    Neighbors of 16 should be 11, 12, 15 (in any order)
    """
    # Checking the bottom-right corner (value 16)
    assert len(find_neighbor_values(GRID, 3, 3)) == len([11, 12, 15])
    # Verifying the correct neighbors (11, 12, and 15)
    assert set(find_neighbor_values(GRID, 3, 3)) == set([11, 12, 15])

def test_find_neighbours_left_edge():
    """
    Edge cell (left edge)
    Neighbors of 5 should be 1, 2, 6, 9, 10 (in any order)
    """
    # Testing a cell on the left edge (value 5)
    assert len(find_neighbor_values(GRID, 1, 0)) == len([1, 2, 6, 9, 10])
    # Checking I get all five correct neighbors
    assert set(find_neighbor_values(GRID, 1, 0)) == set([1, 2, 6, 9, 10])

def test_find_neighbor_values_top_edge():
    """
    Edge cell (top edge)
    Neighbors of 2 should be 1, 3, 5, 6, 7 (in any order)
    """
    # Looking at a cell on the top edge (value 2)
    assert len(find_neighbor_values(GRID, 0, 1)) == len([1, 3, 5, 6, 7])
    # Verifying its five neighbors
    assert set(find_neighbor_values(GRID, 0, 1)) == set([1, 3, 5, 6, 7])

def test_find_neighbor_values_right_edge():
    """
    Edge cell (right edge)
    Neighbors of 8 should be 3, 4, 7, 11, 12 (in any order)
    """
    # Testing a cell on the right edge (value 8)
    assert len(find_neighbor_values(GRID, 1, 3)) == len([3, 4, 7, 11, 12])
    # Making sure I get all five correct neighbors
    assert set(find_neighbor_values(GRID, 1, 3)) == set([3, 4, 7, 11, 12])

def test_find_neighbor_bottom_edge():
    """
    Edge cell (bottom edge)
    Neighbors of 15 should be 10, 11, 12, 14, 16 (in any order)
    """
    # Checking a cell on the bottom edge (value 15)
    assert len(find_neighbor_values(GRID, 3, 2)) == len([10, 11, 12, 14, 16])
    # Verifying its five neighbors
    assert set(find_neighbor_values(GRID, 3, 2)) == set([10, 11, 12, 14, 16])

def test_find_neighbor_middle():
    """
    Middle cell
    Neighbors of 6 should be 1, 2, 3, 5, 7, 9, 10, 11 (in any order)
    """
    # Testing a cell in the middle (value 6) which has the most neighbors
    assert len(find_neighbor_values(GRID, 1, 1)) == len([1, 2, 3, 5, 7, 9, 10, 11])
    # Verifying all eight neighbors are correct
    assert set(find_neighbor_values(GRID, 1, 1)) == set([1, 2, 3, 5, 7, 9, 10, 11])