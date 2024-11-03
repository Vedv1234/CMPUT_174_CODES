# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: In this version, I expanded my age comparison program to work with both Frodo and Gollum.
# I wanted to make things more interesting by adding another character, which meant I needed to handle more complex
# comparison scenarios. This helped me practice nested conditions and multiple character comparisons.

# First I'm setting up my constant ages that I'll use for comparison
frodo_age = 51  # I'm keeping Frodo's age the same as before
gollum_age = 589  # Added Gollum's age - he's quite old!

# Getting the user's input just like in my first version
character_name = input("Please enter the name of your character >")  # First I ask for the character name
character_age = int(input("Please enter the age of your character >"))  # Then I get their age and make it an integer

# Now I'm doing more complex comparisons with both characters
if character_age > frodo_age and character_age > gollum_age:  # I check if they're older than both characters
    print(f"{character_name} is {character_age} years old, and they are older than Gollum and Frodo.")  # If true, they're the oldest
elif character_age > frodo_age and character_age < gollum_age:  # Check if they're between Frodo and Gollum's ages
    print(f"{character_name} is {character_age} years old, and they are older than Frodo but younger than Gollum")  # Tell them they're in the middle
else:  # If neither of those is true, they must be younger than both
    print(f"{character_name} is {character_age} years old, and they are younger than Gollum and Frodo.")  # Let them know they're the youngest