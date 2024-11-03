"""
Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
Functionality of code: This is my test file for yahtzee1.py where I've created various test cases 
to make sure my upper section scoring functions work correctly. I've included tests for different 
dice combinations to thoroughly check my scoring logic.
"""

# I'm importing the functions I need to test from my yahtzee1.py file
from yahtzee1 import sum_of_given_number, fill_upper_section 

def test_sum_of_given_number_all_different():
    """
    In this test, I'm checking how my function handles a roll where all dice show different numbers.
    This helps me verify that my function correctly counts single occurrences.
    """
    # I'm using a roll where each die shows a different number to test all possibilities
    roll = (1, 2, 3, 4, 5)  
    # Now I'm checking each possible number (1-6) to make sure it counts correctly
    assert sum_of_given_number(roll, 1) == 1  # Should find only one '1'
    assert sum_of_given_number(roll, 2) == 2  # Should find only one '2'
    assert sum_of_given_number(roll, 3) == 3  # Should find only one '3'
    assert sum_of_given_number(roll, 4) == 4  # Should find only one '4'
    assert sum_of_given_number(roll, 5) == 5  # Should find only one '5'
    assert sum_of_given_number(roll, 6) == 0  # Should find no '6's

def test_sum_of_given_number_all_same():
    """
    Here I'm testing how my function handles when all dice show the same number.
    This is important for checking maximum possible scores.
    """
    # I've set up a roll where all dice show 3
    roll = (3, 3, 3, 3, 3)
    # Now I'm verifying that it correctly handles this special case
    assert sum_of_given_number(roll, 1) == 0   # Should find no '1's
    assert sum_of_given_number(roll, 2) == 0   # Should find no '2's
    assert sum_of_given_number(roll, 3) == 15  # Should find five '3's (5 * 3 = 15)
    assert sum_of_given_number(roll, 4) == 0   # Should find no '4's
    assert sum_of_given_number(roll, 5) == 0   # Should find no '5's
    assert sum_of_given_number(roll, 6) == 0   # Should find no '6's

def test_sum_of_given_number_some_different():
    """
    In this test, I'm checking how my function handles a mix of repeated and single numbers.
    This represents a more typical roll in an actual game.
    """
    # I've created a roll with some repeated numbers to test this case
    roll = (2, 3, 2, 4, 3)
    # Testing each possible number to ensure correct counting
    assert sum_of_given_number(roll, 1) == 0  # Should find no '1's
    assert sum_of_given_number(roll, 2) == 4  # Should find two '2's (2 * 2 = 4)
    assert sum_of_given_number(roll, 3) == 6  # Should find two '3's (2 * 3 = 6)
    assert sum_of_given_number(roll, 4) == 4  # Should find one '4'
    assert sum_of_given_number(roll, 5) == 0  # Should find no '5's
    assert sum_of_given_number(roll, 6) == 0  # Should find no '6's

def test_fill_upper_section():
    """
    This is my test for the fill_upper_section function to make sure it creates
    the correct score list for the upper section.
    """
    # I'm using a specific roll to test the complete upper section scoring
    roll = (3, 2, 4, 4, 6)
    # Checking if my function returns the correct scores for each number 1-6
    assert fill_upper_section(roll) == [0, 2, 3, 8, 0, 6]  # Each position represents scores for 1s through 6s

# This lets me run my tests using pytest when I run this file directly
if __name__ == "__main__":
    import pytest
    pytest.main()