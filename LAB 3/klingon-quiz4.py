# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my final version of the Klingon quiz where I added
# random hints! Now on the second attempt, I reveal a random letter in the middle of
# the word to make it more interesting. It's like a game show where you get
# progressively more helpful clues!

# I need the random module for my new hint feature
import random

# My cleaned up list of valid Klingon consonants
valid_consonants = ['b', 'ch', 'D', 'gh', 'H', 'j', 'l', 'm', 'n', 'p', 'q', 'Q', 'r', 'S', 't', 'v', 'w', 'y']

# Opening my translation file
with open('klingon-english.txt', mode='r', encoding='utf-8') as file:
    # Getting all my lines
    lines = file.readlines()

# Setting up my set of unique Klingon consonants
klingon_consonants = set()
for line in lines:
    klingon_word = line.split('|')[1].strip()
    klingon_consonants.add(klingon_word[0])

# Getting the user's chosen consonant
chosen_consonant = input("Choose a Klingon consonant to practice with: ")

# Making sure it's valid
while chosen_consonant not in valid_consonants:
    print("Invalid consonant. Please choose a valid Klingon consonant.")
    chosen_consonant = input("Choose a Klingon consonant to practice with: ")

# Finding a word with their chosen consonant
chosen_word = ""
correct_word = ""
for line in lines:
    if line.startswith(chosen_consonant):
        chosen_word = line.split('|')[1].strip()
        correct_word = line.split('|')[0].strip()
        break

# Setting up my attempt counters
attempts = 0
max_attempts = 3
ra = 3

# Giving them their attempts with my new hint system
while attempts < max_attempts:
    # Asking for their translation
    user_translation = input(f"Attempt {attempts + 1}: Translate the word {chosen_word} into Klingon. You have {ra} attempts left: ")

    # Checking their answer
    if user_translation.lower() == correct_word.lower():
        print("Correct!")
        break
    else:
        # Creating my hint - starts with just first and last letters
        hint = [correct_word[0]] + ['*'] * (len(correct_word) - 2) + [correct_word[-1]]

        # On second attempt, I reveal a random middle letter
        if attempts == 1:
            random_index = random.randint(1, len(correct_word) - 2)
            hint[random_index] = correct_word[random_index]
        ra = ra - 1
        
        if ra > 0 and ra <= 3:
            print(f"Sorry, you're wrong! Hint: {''.join(hint)}")
        attempts += 1

# If they're out of attempts, show the answer
if attempts == max_attempts:
    print(f"Sorry, you've run out of attempts. The correct answer is {correct_word}")