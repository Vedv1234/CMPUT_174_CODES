# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: My third version adds a scoring system to make it more
# game-like! Players get 10 points for correct spells and lose 5 for mistakes.
# I also added the option to keep practicing with more spells. It's starting to
# feel like a real game now!

import random  # For picking random spells

def read_spells(filename:str) -> list[str]:
    """
    Returns a random spell from a list of spells, converted to lowercase.
    """
    # Reading my spells from the file
    with open(filename,'r') as file:
        spells = file.read().splitlines()  # Making a list where each spell is one element
        return spells

def get_random_spell(spells: list[str]) -> str:
    """
    Returns a random spell from a list of spells, converted to lowercase.
    """
    # Picking a random spell for the user to practice
    return random.choice(spells).lower()

def display_header():
    """
    Displays header as follows:
    ############################################################
    Harry Potter Typing Trainer
    ############################################################
    """
    # My cool header design
    print(60*"#")  # Top border
    print("Harry Potter Typing Trainer")  # Title
    print(60*"#")  # Bottom border
    
def display_instructions():
    """
    Displays instructions from instructions.txt
    """
    # Showing my instructions to the user
    with open("instructions.txt","r") as file:
        instructions = file.read()
        print(instructions)
        
def get_user_input(spell: str) -> str:
    """
    Gets the spell as input from the user and returns it.
    """
    # Getting the user's attempt at typing the spell
    print("Type the following spell: " + spell)
    user_input = input()
    return user_input.lower()  # Making it lowercase for fair comparison

def display_feedback(spell: str, user_input: str):
    """
    Displays feedback (correct or incorrect) to the user.
    """
    # Telling the user if they got it right
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
    # Asking if they want to try another spell
    play = input("Do you want to practice more? (Y/N) :").lower().strip()
    return play == 'y'  # They can continue if they type 'y' or 'Y'
    
def main() -> None:
    """
    Main program.
    """
    # Setting up my game
    spells = read_spells('spells.txt')
    display_header()
    display_instructions()
    score = 0  # Starting score at zero
    user_playing = True  # This lets me keep the game running
    
    # My main game loop
    while user_playing == True:
        spell = get_random_spell(spells)  # Getting a new spell
        user_input = get_user_input(spell)  # Getting their attempt
        if user_input == spell:
            score = score + 10  # They get 10 points for getting it right
            print("Correct!")
            print(f"You get 10 points! Your Score is: {score}")
        else:
            score = score - 5  # Taking away 5 points for mistakes
            print("Incorrect!")
            print(f"The spell was : {spell}")
            print(f"You lose! Your score is:{score}")
            
        user_playing = play_again()  # Checking if they want to continue
        
    print(f" Final Score : {score}")  # Showing their final score when they finish
    
if __name__ == "__main__":
    main()