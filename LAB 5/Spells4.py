# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my final and most advanced version! I added a timing
# system where users have to type spells quickly to get full points. It calculates
# target times based on spell length and gives different points depending on how fast
# they type. I'm really proud of how professional it turned out!

import random  # For my random spell selection
import time  # I need this to measure typing speed

def read_spells(filename:str) -> list[str]:
    """
    Returns a random spell from a list of spells, converted to lowercase.
    """
    # Opening my spells file
    with open(filename,'r') as file:
        spells = file.read().splitlines()  # Creating my list of spells
        return spells

def get_random_spell(spells: list[str]) -> str:
    """
    Returns a random spell from a list of spells, converted to lowercase.
    """
    # Picking a random spell and making it lowercase
    return random.choice(spells).lower()

def display_header():
    """
    Displays header as follows:
    ############################################################
    Harry Potter Typing Trainer
    ############################################################
    """
    # My program header - made it look nice!
    print(60*"#")
    print("Harry Potter Typing Trainer")
    print(60*"#")
    
def display_instructions():
    """
    Displays instructions from instructions.txt
    """
    # Showing my instructions to the user
    with open("instructions.txt","r") as file:
        instructions = file.read()
        print(instructions)
        
def get_user_input(spell: str) -> (str, float):
    """
    Gets input from the user
    Returns the input and the time it took the user to type the input
    """
    # This is my fancy new timing system!
    start = time.time()  # Starting my timer
    print(f"Type the following spell: {spell}")
    user_input = input().lower()  # Getting their attempt
    user_time = round(time.time() - start, 2)  # Calculating how long they took
    print(f"Result: {user_time} seconds (goal: {get_target_time(spell)} seconds).")
    return user_input, user_time

def display_feedback(spell: str, user_input: str):
    """
    Displays feedback (correct or incorrect) to the user.
    """
    # Telling them if they got the spell right
    if user_input == spell:
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The spell was: {spell}")
        
def play_again() -> bool:
    """
    Asks the user if they want to play again
    Returns True if the user enters Y or y, False otherwise
    """
    # Checking if they want another round
    play = input("Do you want to practice more? (Y/N) :").lower().strip()
    return play == 'y'

def get_target_time(spell: str) -> float:
    """
    Returns the target time to type the spell.
    """
    # My formula for calculating target typing time
    TTT = len(spell) * 0.3  # I give them 0.3 seconds per character
    return TTT

def calculate_points(spell: str, user_input: str, user_time: float) -> int:
    """
    Calculates the points that the user gets based on correctness and time.
    """
    target_time = get_target_time(spell)  # Getting my target time

    # My new scoring system based on speed and accuracy
    if user_input.lower() == spell.lower():
        if user_time <= target_time:  # Full points for fast and accurate
            return 10
        elif user_time <= target_time * 1.5:  # Partial points if they're a bit slow
            return 6
        elif user_time <= target_time * 2:  # Fewer points if they're quite slow
            return 3
        else:  # Just one point if they're very slow
            return 1
    else:
        return -5  # Still taking points off for mistakes

def main() -> None:
    """
    Main program.
    """
    # Setting up my game
    spells = read_spells('spells.txt')
    display_header()
    display_instructions()
    score = 0
    playing = True

    # My main game loop with the new timing system
    while playing == True:
        spell = get_random_spell(spells)
        user_input, user_time = get_user_input(spell)  # Now I'm tracking their time too
        points_achieved = calculate_points(spell, user_input, user_time)

        # Giving them feedback about their performance
        if points_achieved > 0:
            print("Correct!")
            print(f"You get {points_achieved} points!, Score: {score + points_achieved}")
        else:
            print("Incorrect!")
            print(f"The spell was: {spell}")
            print(f"You get {points_achieved} points!, Score: {score + points_achieved}")

        score = score + points_achieved  # Updating their score
        playing = play_again()  # Checking if they want to continue

    print(f"Final Score: {score}")  # Showing their final score

if __name__ == "__main__":
    main()