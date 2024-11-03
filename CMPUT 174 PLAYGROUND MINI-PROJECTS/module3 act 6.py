# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my word puzzle helper for Mr. Ratburn that finds
# all 3-letter words that start and end with the same letter. It helps create
# an answer key for his word-search puzzle.

'''Mr. Ratburn has created a word-search puzzle for his students. He has asked them to identify all 3 letter words in the puzzle that start and end with the same letter. Mr. Ratburn needs help to prepare an answer key for the puzzle.

Create a program that searches through a list of words and prints all 3 letter words that start and end with the same letter.
'''

# My list of words to check
words = ['aha', 'area', 'bulbs', 'chic', 'dad', 'wow', 'tact', 'pulp', 'pump', 'mom']

# I'm checking each word for the conditions:
# 1. Must be 3 letters long
# 2. First and last letters must match
for word in words:
    if len(word) == 3 and word[0] == word[len(word)-1]:
        print(word)