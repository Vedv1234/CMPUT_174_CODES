# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my first version of the Harry Potter typing trainer! 
# I started with something simple - just reading spells from a file and displaying
# them randomly. I wanted to make a fun way to practice typing with Harry Potter spells.

import random  # I'm using this to pick random spells

def read_spells(filename:str) -> list[str]:
    """
    Returns a random spell from a list of spells, converted to lowercase.
    """
    # I'm opening my spells file and reading it line by line
    with open(filename,'r') as file:
        spells = file.read().splitlines()  # This splits my file into a list where each spell is one element
        return spells  # Sending back my list of spells

def get_random_spell(spells: list[str]) -> str:
    """
    Returns a random spell from a list of spells, converted to lowercase.
    """
    # I added this check to handle empty spell lists
    if not spells:
        no_result = "No spells found"
        return no_result
    return random.choice(spells).lower()  # Picking a random spell and making it lowercase

def main() -> None:
    """
    Main program.
    """
    # Here's where I tie everything together
    spells = read_spells('spells.txt')  # First I read my spells file
    print('Harry Potter Keyboard Trainer')  # Showing my program title
    spell = get_random_spell(spells)  # Getting a random spell
    print(spell)  # Displaying the spell to the user

if __name__ == "__main__": # I learned this new style in class - it's the proper way to run the main function
        main()