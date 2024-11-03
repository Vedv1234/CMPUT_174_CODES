# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: In this second version, I expanded my typing trainer to actually
# test the user's typing skills! Now it shows instructions, asks for input, and checks
# if they typed the spell correctly. I also added a cool header to make it look more
# professional.

import random  # Need this for my random spell selection

def read_spells(filename:str) -> list[str]:
    """
    Returns a random spell from a list of spells, converted to lowercase.
    """
    # Opening my file that contains all the Harry Potter spells
    with open(filename,'r') as file:
        spells = file.read().splitlines()  # Converting my file into a list of spells
        return spells

def get_random_spell(spells: list[str]) -> str:
    """
    Returns a random spell from a list of spells, converted to lowercase.
    """
    # I'm picking a random spell and making it lowercase for easier comparison later
    return random.choice(spells).lower()

def display_header():
    """
    Displays header as follows:
    ############################################################
    Harry Potter Typing Trainer
    ############################################################
    """
    # I made this cool header to make my program look more professional
    print(60*"#")  # Making a line of hashtags for the top
    print("Harry Potter Typing Trainer")  # My program title
    print(60*"#")  # Bottom line of hashtags
    
def display_instructions():
    """
    Displays instructions from instructions.txt
    """
    # Reading and showing the instructions I wrote for users
    with open("instructions.txt","r") as file:
        instructions = file.read()
        print(instructions)
        
def get_user_input(spell: str) -> str:
    """
    Gets the spell as input from the user and returns it.
    """
    # This is where I ask the user to type the spell
    print("Type the following spell: " + spell)
    user_input = input()
    return user_input.lower()  # Converting to lowercase to make comparison fair

def display_feedback(spell: str, user_input: str):
    """
    Displays feedback (correct or incorrect) to the user.
    """
    # Here I check if they got it right and give them feedback
    if user_input == spell:
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The spell was: {spell}")  # Showing them the right spell if they made a mistake
        
def main() -> None:
    """
    Main program.
    """
    # This is where I put everything together
    spells = read_spells('spells.txt')  # Getting my list of spells
    spell = get_random_spell(spells)  # Picking a random one
    display_header()  # Showing my cool header
    display_instructions()  # Displaying the instructions
    user_input = get_user_input(spell)  # Getting what the user typed
    display_feedback(spell, user_input)  # Telling them if they got it right

if __name__ == "__main__": # Using the proper way to run my main function
        main()