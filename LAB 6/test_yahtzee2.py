"""
Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
Functionality of code: This is my test file for yahtzee2.py where I'm testing the lower section 
scoring functions. I've included comprehensive tests for three-of-a-kind, four-of-a-kind, and 
Yahtzee combinations to ensure my scoring logic works perfectly.
"""

# I'm importing the specific functions I need to test from my yahtzee2.py file
from yahtzee2 import num_of_a_kind, yahtzee

def test_three_of_a_kind_found():
    """
    Here I'm testing if my function correctly identifies when there are exactly three dice
    showing the same number.
    """
    # I'm using a roll with three 3's to test three-of-a-kind
    roll = (3, 3, 3, 4, 5)
    # Checking if it correctly returns the sum of all dice (3+3+3+4+5 = 18)
    assert num_of_a_kind(roll, 3) == 18

def test_three_of_a_kind_not_found():
    """
    I'm making sure my function returns 0 when there isn't a three-of-a-kind in the roll.
    """
    # Using a roll with all different numbers
    roll = (1, 2, 3, 4, 5)
    # Making sure it returns 0 when there's no three-of-a-kind
    assert num_of_a_kind(roll, 3) == 0

def test_four_of_a_kind_found():
    """
    This test checks if my function correctly identifies four dice showing the same number.
    """
    # Setting up a roll with four 4's to test four-of-a-kind
    roll = (4, 4, 4, 4, 5)
    # Verifying it returns the correct sum (4+4+4+4+5 = 21)
    assert num_of_a_kind(roll, 4) == 21

def test_four_of_a_kind_not_found():
    """
    I'm testing that my function returns 0 when there isn't a four-of-a-kind present.
    """
    # Using a roll with all different numbers again
    roll = (1, 2, 3, 4, 5)
    # Checking that it correctly returns 0 when no four-of-a-kind is found
    assert num_of_a_kind(roll, 4) == 0

def test_yahtzee_found():
    """
    Here I'm testing if my function correctly identifies a Yahtzee (all five dice showing
    the same number).
    """
    # Creating a perfect Yahtzee roll with all 5's
    roll = (5, 5, 5, 5, 5)
    # Verifying it returns 50 points for a Yahtzee
    assert yahtzee(roll) == 50

def test_yahtzee_not_found():
    """
    I'm making sure my function returns 0 when the roll isn't a Yahtzee.
    """
    # Using a roll with different numbers
    roll = (1, 2, 3, 4, 5)
    # Checking that it returns 0 when it's not a Yahtzee
    assert yahtzee(roll) == 0

# This allows me to run my tests using pytest when I run this file directly
if __name__ == "__main__":
    import pytest
    pytest.main()