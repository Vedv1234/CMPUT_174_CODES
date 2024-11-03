# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my improved version of the Klingon quiz where I added
# consonant selection. I wanted to make it more interactive by letting users choose
# which consonant they want to practice with. It's like a more personalized learning
# experience!

# I created a list of all valid Klingon consonants to check against - these are all the ones they can pick from
valid_consonants=['b', 'ch', 'D', 'gh', 'H', 'j',' l', 'm', 'n', 'p', 'q', 'Q',' r', 'S', 't',' v', 'w',' y']

# I need to open my translation file again - still using UTF-8 to handle any special characters
with open('klingon-english.txt', mode='r', encoding='utf-8') as file:
    # Loading all my lines into memory - I'll search through these for words
    lines = file.readlines()

# I'm making an empty set to collect unique Klingon consonants as I find them
klingon_consonants = set()
for line in lines:
    # Splitting each line to get just the Klingon word part
    klingon_word = line.split('|')[1]  

# This is where my users get to pick which consonant they want to practice
chosen_consonant = input("Choose a Klingon consonant to practice with: ")

# I'm making sure they don't try to use invalid consonants - this loop keeps asking until they pick a good one
while chosen_consonant not in valid_consonants:
    print("Invalid consonant. Please choose a valid Klingon consonant.")
    chosen_consonant = input("Choose a Klingon consonant to practice with: ")

# Now I'm hunting through my word list to find one that starts with their chosen consonant
chosen_word = ""
for line in lines:
    if line.startswith(chosen_consonant):
        chosen_word = line.split('|')[1]
        correct_word= line.split('|')[0]
        break

# Time to test their knowledge! I show them the word and ask for the translation
user_translation = input(f"Translate the word {chosen_word} into Klingon: ")

# Checking their answer - I made it case-insensitive this time to be more forgiving
if user_translation.lower() == correct_word.lower():
    print("Correct!")
else:
    print(f"Sorry, you're wrong! The correct answer is {correct_word}")