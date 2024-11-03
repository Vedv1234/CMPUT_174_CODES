# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my final version of the Klingon quiz where I added
# random hints! Now on the second attempt, I reveal a random letter in the middle of
# the word to make it more interesting. It's like a game show where you get
# progressively more helpful clues!

# I need random for my new hint feature - this will help make the hints more interesting
import random

# My final, perfectly organized list of Klingon consonants
valid_consonants = ['b', 'ch', 'D', 'gh', 'H', 'j', 'l', 'm', 'n', 'p', 'q', 'Q', 'r', 'S', 't', 'v', 'w', 'y']

# Opening my translation file one last time - still being careful with character encoding
with open('klingon-english.txt', mode='r', encoding='utf-8') as file:
    # Loading up all my translation pairs
    lines = file.readlines()

# Setting up my consonant set - this worked well in previous versions
klingon_consonants = set()
for line in lines:
    # Using my improved whitespace handling from version 3
    klingon_word = line.split('|')[1].strip()
    klingon_consonants.add(klingon_word[0])

# Getting the user's consonant choice - kept this consistent through versions
chosen_consonant = input("Choose a Klingon consonant to practice with: ")

# My reliable validation loop - making sure they pick a valid consonant
while chosen_consonant not in valid_consonants:
    print("Invalid consonant. Please choose a valid Klingon consonant.")
    chosen_consonant = input("Choose a Klingon consonant to practice with: ")

# Finding a word with their chosen consonant - using my clean whitespace handling
chosen_word = ""
correct_word = ""
for line in lines:
    if line.startswith(chosen_consonant):
        chosen_word = line.split('|')[1].strip()
        correct_word = line.split('|')[0].strip()
        break

# Setting up my attempt tracking - keeping the 3-attempt limit from version 3
attempts = 0
max_attempts = 3
ra = 3

# My improved loop with random hints - this is the cool new part!
while attempts < max_attempts:
    # Asking for their translation - showing attempt count and remaining tries
    user_translation = input(f"Attempt {attempts + 1}: Translate the word {chosen_word} into Klingon. You have {ra} attempts left: ")

    # Checking their answer - still case-insensitive for user-friendliness
    if user_translation.lower() == correct_word.lower():
        print("Correct!")
        break
    else:
        # Creating my new hint system - starts with just first and last letters
        hint = [correct_word[0]] + ['*'] * (len(correct_word) - 2) + [correct_word[-1]]

        # On second attempt, I reveal a random middle letter - this makes it more fun!
        if attempts == 1:
            random_index = random.randint(1, len(correct_word) - 2)
            hint[random_index] = correct_word[random_index]
        ra = ra - 1
        
        if ra > 0 and ra <= 3:
            print(f"Sorry, you're wrong! Hint: {''.join(hint)}")
        attempts += 1

# Still showing the correct answer if they run out of attempts - learning is important!
if attempts == max_attempts:
    print(f"Sorry, you've run out of attempts. The correct answer is {correct_word}")