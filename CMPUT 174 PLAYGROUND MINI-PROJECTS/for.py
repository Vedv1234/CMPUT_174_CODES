# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my program that works with lists to find words 
# that start with vowels. When it finds a word starting with a vowel, it moves
# it to the beginning of the list.

# I'm setting up my lists of vowels and words to check
vowels = ['a', 'e', 'i', 'o', 'u']
words = ['castle', 'apple', 'markers', 'pencil', 'elephants']

# I'm going through each word in my list
for i in range(len(words)):
    word = words[i]
    # If I find a word that starts with a vowel
    if word[0] in vowels:
        # I remove it from its current position
        words.pop(i)
        # And put it at the start of the list
        words.insert(0, word)
print(words)