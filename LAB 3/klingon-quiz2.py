# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my improved version of the Klingon quiz where I added
# consonant selection. I wanted to make it more interactive by letting users choose
# which consonant they want to practice with. It's like a more personalized learning
# experience!

# I created a list of all valid Klingon consonants to check against
valid_consonants=['b', 'ch', 'D', 'gh', 'H', 'j',' l', 'm', 'n', 'p', 'q', 'Q',' r', 'S', 't',' v', 'w',' y']

# Opening my translation file - same UTF-8 encoding as before
with open('klingon-english.txt', mode='r', encoding='utf-8') as file:
    # Getting all my lines into a list again
    lines = file.readlines()

# I'm creating an empty set to store unique Klingon consonants
klingon_consonants = set()
for line in lines:
    # For each line, I'm getting just the Klingon word part
    klingon_word = line.split('|')[1]  

# Here's where I let the user pick which consonant they want to practice
chosen_consonant = input("Choose a Klingon consonant to practice with: ")

# I'm making sure they pick a valid consonant - if not, I'll keep asking
while chosen_consonant not in valid_consonants:
    print("Invalid consonant. Please choose a valid Klingon consonant.")
    chosen_consonant = input("Choose a Klingon consonant to practice with: ")

# Looking for a word that starts with their chosen consonant
chosen_word = ""
for line in lines:
    if line.startswith(chosen_consonant):
        chosen_word = line.split('|')[1]
        correct_word= line.split('|')[0]
        break

# Time for them to try translating the word!
user_translation = input(f"Translate the word {chosen_word} into Klingon: ")

# Checking their answer and giving feedback
if user_translation.lower() == correct_word.lower():
    print("Correct!")
else:
    print(f"Sorry, you're wrong! The correct answer is {correct_word}")