# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my first attempt at creating a simple Klingon language quiz.
# I wanted to make something that could help people practice translating words between
# Klingon and English. It's pretty straightforward - it just asks for one translation
# and checks if you got it right.

# I'm opening my translation file here - making sure to use UTF-8 since Klingon might have special characters
with open('klingon-english.txt', mode='r', encoding='utf-8') as file:
    # Reading all the lines from my file into a list - I'll need these for the quiz
    lines = file.readlines()

# I'm grabbing the third line and splitting it by the | character
# The strip() removes any extra whitespace that might mess up my comparison later
third_line_split = (lines[2].strip()).split('|') 

# Here's where I ask the user to translate the word - I'm showing them the English version
user_translation = input(f"Translate the word {(third_line_split[1])} into Klingon: ")

# I'm storing the correct Klingon translation to compare against
correct_translation = third_line_split[0]

# Now I check if they got it right and let them know
if user_translation == correct_translation:
    print("Correct!")
else:
    print(f"Sorry, you're wrong! The correct answer is {correct_translation}")