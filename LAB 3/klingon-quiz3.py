# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: In this version, I added multiple attempts and hints to make
# my quiz more forgiving and helpful. I give users 3 tries to get the right answer,
# and I show them hints after wrong attempts. It's like having a patient Klingon
# teacher!

# My list of valid Klingon consonants - I cleaned up the spacing from the previous version
valid_consonants = ['b', 'ch', 'D', 'gh', 'H', 'j', 'l', 'm', 'n', 'p', 'q', 'Q', 'r', 'S', 't', 'v', 'w', 'y']

# Opening my file with the translations
with open('klingon-english.txt', mode='r', encoding='utf-8') as file:
    # Getting all my lines again
    lines = file.readlines()

# Creating my set of unique Klingon consonants from the file
klingon_consonants = set()
for line in lines:
    # I'm being more careful with whitespace this time using strip()
    klingon_word = line.split('|')[1].strip()
    klingon_consonants.add(klingon_word[0])

# Letting the user choose their consonant
chosen_consonant = input("Choose a Klingon consonant to practice with: ")

# Making sure they pick a valid one
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

# Setting up my attempt counter and limits
attempts = 0
max_attempts = 3
ra = 3  # This keeps track of remaining attempts

# Giving them multiple tries to get it right
while attempts < max_attempts:
    # Asking for their translation
    user_translation = input(f"Attempt {attempts + 1}: Translate the word {chosen_word} into Klingon:  you have {ra} attempts left: ")

    # Checking their answer
    if user_translation.lower() == correct_word.lower():
        print("Correct!")
        break
    else:
        # Creating a hint that shows first and last letters
        hint = correct_word[0] + '*' * (len(correct_word) - 2) + correct_word[-1]
        attempts += 1
        ra = ra - 1
        if ra > 0 and ra < 3:
            print(f"Sorry, you're wrong! Hint: {hint}, you have {ra} attempts left")

# If they use all their attempts, show them the right answer
if attempts == max_attempts:
    print(f"Sorry, you've run out of attempts. The correct answer is {correct_word}")