# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my experimentation with different ways to read files
# in Python. I tried multiple methods and commented out the ones I wasn't currently using.

# Setting up my file details
filename = "employees.txt"
mode = 'r'

'''
# Method 1: I tried reading the whole file at once
content = file.read()
print(content)
print(repr(content))
file.close()

# Method 2: I tried reading the file line by line using a for loop
print("method 2 - viewing file as a sequence")
file = open(filename, mode)
for line in file:
    line = line.strip()  # Removing extra whitespace
    print(line)
file.close()
'''

'''
# Method 3: I tried reading one specific line at a time
print("METHOD 3 - READS ONE LINE AT A TIME")
file = open(filename, mode)
line1 = file.readline().strip()
print(line1)
line2 = file.readline().strip()
print(line2)
file.close()
'''

# Method 4: This is my current method - reading all lines into a list
print("METHOD 4 - reads entire file and returns list of lines")
file = open(filename, mode)
listoflines = file.readlines()
print(listoflines)
file.close()

'''
# I made a note about using split() for parsing strings
# If the separator is the same for different parts of strings, use split method
blist = astring.split(',') # comma is separator to help make string into list
'''