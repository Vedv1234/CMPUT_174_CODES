"""
Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
Functionality of code: This is my implementation of the second part of the Yahtzee game 
where I'm handling the lower section scoring. I've added functions for checking three-of-a-kind, 
four-of-a-kind, and Yahtzee combinations.
"""

# I need random for dice rolling and I'm importing my functions from yahtzee1
import random
from yahtzee1 import make_roll, sum_of_given_number, fill_upper_section, display_upper_section

def num_of_a_kind(roll: tuple, number: int) -> int:
    """
    This is my function to check for three-of-a-kind and four-of-a-kind combinations.
    It returns the sum of all dice if we find the right number of matching dice,
    otherwise returns 0.
    """
    # I'm counting how many times each number appears in my roll
    counts = [roll.count(die) for die in roll]
    # If I find exactly the number I'm looking for (3 or 4), I return the sum
    if number in counts:
        return sum(roll)
    # If I don't find what I'm looking for, I return 0
    return 0

def yahtzee(roll: tuple) -> int:
    """
    This is where I check for a Yahtzee - all five dice showing the same number.
    Returns 50 points for a Yahtzee, 0 otherwise.
    """
    # I'm checking if all dice match the first die
    if all(die == roll[0] for die in roll):
        return 50  # Yahtzee!
    return 0  # Not a Yahtzee

def main():
    """
    This is my main function where I put everything together to show the complete
    game scoring.
    """
    # First, I'm rolling the dice and showing what I got
    roll = make_roll()
    print("Rolling the dice...", roll)
    
    # Displaying the upper section scores
    print("Upper section: ")
    upper_section_scores = fill_upper_section(roll)
    display_upper_section(upper_section_scores)
    
    # Now showing the lower section scores
    print("Lower section: ")
    
    # Checking and displaying three-of-a-kind score
    three_of_a_kind_score = num_of_a_kind(roll, 3)
    print(f"3 of a kind: {three_of_a_kind_score}")
    
    # Checking and displaying four-of-a-kind score
    four_of_a_kind_score = num_of_a_kind(roll, 4)
    print(f"4 of a kind: {four_of_a_kind_score}")
    
    # Checking and displaying Yahtzee score
    yahtzee_score = yahtzee(roll)
    print(f"Yahtzee: {yahtzee_score}")

# This lets me run the complete game when I execute this file directly
if __name__ == "__main__":
    main()