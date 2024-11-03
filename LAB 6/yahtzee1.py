"""
Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
Functionality of code: This is my implementation of the first part of the Yahtzee game. 
In this file, I'm handling the dice rolling mechanics and the upper section scoring. 
I've created functions to generate random rolls and calculate scores for ones through sixes.
"""

# I need the random module for generating dice rolls
import random

def make_roll() -> tuple:
    """
    This is my function to simulate rolling five dice. It returns a tuple of five random numbers
    between 1 and 6.
    """
    # I'm using a list comprehension to generate 5 random numbers and convert them to a tuple
    return tuple(random.randint(1,6) for i in range(5))

def sum_of_given_number(roll: tuple, number: int) -> int:
    """
    This is where I calculate the sum of all dice showing a specific number.
    For example, if I'm looking for 6's and I have (2,6,2,6,1), it should return 12.
    """
    # I'm using a list comprehension to sum up only the dice that match my target number
    return sum(value for value in roll if value == number)

def fill_upper_section(roll: tuple) -> list:
    """
    Here I'm creating a list of scores for the upper section (ones through sixes) based on
    the current roll.
    """
    # I'll store all my scores in this list
    upper_section_scores = []
    # I'm checking each possible die value (1-6)
    for num in range(1,7):
        # Getting the score for the current number and adding it to my list
        score = sum_of_given_number(roll,num)
        upper_section_scores.append(score)
    return upper_section_scores

def display_upper_section(upper_section_scores: list) -> None:
    """
    This is my function to show the upper section scores in a nice format.
    """
    # These are the category names I'll use for display
    names = ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']
    # I'm printing each category with its score
    for i in range(6):
        print(f" {names[i]}: {upper_section_scores[i]}")

def main():
    """
    This is my main function that ties everything together.
    """
    # First, I'm rolling the dice and showing the result
    random_roll = make_roll()
    print("Rolling the dice...", random_roll)
    
    # Now I'm calculating all the upper section scores
    upper_section_scores = fill_upper_section(random_roll)
    
    # Finally, I'm displaying all the scores
    display_upper_section(upper_section_scores)

# This lets me run the game when I execute this file directly
if __name__ == "__main__":
    main()