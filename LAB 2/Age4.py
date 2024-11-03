# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my final and most sophisticated version of the age comparison program. 
# I decided to use lists and loops to make the code more efficient and handle multiple characters more elegantly.
# This shows how I've progressed from simple if-else statements to more advanced Python concepts.

# I created lists to store all my character data
names = [
    "Frodo",
    "Samwise",
    "Gandalf",
    "Legolas",
    "Gimli",
    "Aragorn",
    "Boromir",
    "Merry",
    "Pippin",
]  # I put all the names in one list
ages = [51, 39, 2000, 2931, 140, 88, 41, 37, 29]  # And their corresponding ages in another

# Getting user input like in my previous versions
character_name = input("Enter the name of a character: ")  # Getting their character's name
character_age = int(input("Enter the age of the character: "))  # Getting and converting the age

# I added better age validation
if character_age < 0:  # Checking for negative ages
    print("Invalid age.")  # Tell them if the age is invalid
    exit()  # And exit the program

# I created lists to store my comparison results
names_older = []  # This will hold names of characters older than the user's
names_younger = []  # This will hold names of characters younger than the user's

# I'm using a loop to compare ages - much more efficient than my earlier versions!
for i in range(len(names)):  # Loop through all my characters
    if ages[i] > character_age:  # If this character is older
        names_older.append(names[i])  # Add them to my older list
    elif ages[i] < character_age:  # If this character is younger
        names_younger.append(names[i])  # Add them to my younger list

# Finally, I display the results in a nice format
if names_older != []:  # If we found any older characters
    print(f"{character_name} is {character_age} years old,he is younger than", ', '.join(names_older))
if names_younger != []:  # If we found any younger characters
    print(f"{character_name} is {character_age} years old,he is older than", ', '.join(names_younger))