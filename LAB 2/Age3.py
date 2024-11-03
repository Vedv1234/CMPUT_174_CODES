# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my third iteration where I really stepped up the complexity. I added even more
# characters (Pippin and Arwen) and included age validation. I wanted to make the program more robust and 
# handle more interesting age comparisons. This version shows how much I've learned about nested conditions.

# Setting up all my character ages as constants
pippin_age = 29  # Added Pippin - he's the youngest
frodo_age = 51  # Keeping Frodo's age constant
gollum_age = 589  # Gollum is still pretty old
arwen_age = 2901  # Added Arwen - she's the eldest!

# Getting user input like in my previous versions
character_name = input("Please enter the name of your character >")  # Getting character name
character_age = int(input("Please enter the age of your character >"))  # Getting and converting age to integer

# I added age validation this time
if character_age == -1:  # First I check if they entered an invalid age
    print("Invalid age")  # Let them know if they did

if character_age != -1:  # If the age is valid, I proceed with my comparisons
    # Now I'm doing some complex nested comparisons
    if character_age < frodo_age and character_age < gollum_age and character_age < pippin_age and character_age < arwen_age:  
        # If they're younger than everyone
        print(f"{character_name} is {character_age} years old, and they are younger than Arwen, Gollum, Frodo, Pippin.")
    elif character_age > frodo_age and character_age > pippin_age and character_age < gollum_age and character_age < arwen_age:
        # If they're older than some but younger than others
        print(f"{character_name} is {character_age} years old, and they are older than Frodo, Pippin.")
        print(f"{character_name} is {character_age} years old, and they are younger than Arwen, Gollum.")
    elif character_age > frodo_age and character_age > gollum_age and character_age > pippin_age and character_age > arwen_age:
        # If they're older than everyone
        print(f"{character_name} is {character_age} years old, and they are older than Arwen, Gollum, Frodo, Pippin.")