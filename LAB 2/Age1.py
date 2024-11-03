# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: I created this program to compare ages between a user's character and Frodo Baggins.
# This was my first attempt at working with character age comparisons, keeping it simple with just one character
# to compare against. I used basic if-else logic to make the comparisons work.

# I'm getting the character info from the user here
character_name = input("Please enter the name of your character >")  # First I ask for their character's name
character_age = int(input("Please enter the age of your character >"))  # Then I get the age and convert it to integer

# I'm setting up Frodo's age as a constant since it won't change
frodo_age = 51  # I hardcoded Frodo's age here since it's a fixed value

# Now I'm doing my age comparisons using if-elif-else
if frodo_age > character_age:  # First I check if Frodo is older
    print(f"{character_name} is {character_age} years old, and they are younger than Frodo.")  # If true, I tell them their character is younger
elif frodo_age < character_age:  # Then I check if the character is older than Frodo
    print(f"{character_name} is {character_age} years old, and they are older than Frodo.")  # If true, I tell them their character is older
else:  # If neither of those conditions are true, they must be the same age
    print(f"{character_name} is {character_age} years old, and they are of the same age as Frodo.")  # So I tell them the ages match