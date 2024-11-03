# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my word sorter program that reorganizes a list
# of words by moving any words that start with vowels to the beginning of the list.

# Setting up my lists
vowels = ['a', 'e', 'i', 'o', 'u']
words = ['castle', 'apple', 'markers', 'pencil', 'elephant']

# I'm checking each word in the list
for index in range(len(words)):
    word = words[index]
    # If I find a word that starts with a vowel
    if word[0] in vowels:
        # I remove it from its current position
        words.pop(index)
        # And move it to the front of the list
        words.insert(0, word)