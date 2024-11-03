# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my program that uses an imported function to find
# the longest word in a list of programming languages. It shows how I can import
# and use functions from other files.

# I'm importing a specific function from my testing module
from testing import find_longest_word

# My list of programming languages to check
languages = ['c', 'java', 'python', 'fortran', 'ruby']
# Using my imported function to find the longest language name
print(find_longest_word(languages))