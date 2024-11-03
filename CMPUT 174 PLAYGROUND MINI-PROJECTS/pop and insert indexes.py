# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my word sorter program that reorganizes a list
# by moving words that start with vowels to the front of the list.

# My lists of vowels and words to check
vowels = ['a', 'e', 'i', 'o', 'u']
words = ['castle', 'apple', 'markers', 'pencil', 'elephants']

# Going through my word list with index access
for i in range(len(words)):
    word = words[i]
    # If I find a word starting with a vowel
    if word[0] in vowels:
        # I remove it from its current spot
        words.pop(i)
        # And move it to the front
        words.insert(0, word)

print(words)