# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: In this mini project, I'm exploring how to use the replace() method 
# in Python strings. My goal is to replace each number in a string with the letter 'a'.
# This helped me understand string manipulation better.

# Here I'm creating my initial string with numbers 1 through 5 separated by spaces
astring = '1 2 3 4 5'

# I'm using a for loop that goes from 1 to 5 (inclusive) to replace each number
for i in range(1,6):
    # In each iteration, I'm replacing the current number (converted to string) with 'a'
    # The replace() method creates a new string each time, so I need to store it back in astring
    astring = astring.replace(str(i),'a')
    
# Finally, I'm printing my modified string to see all numbers replaced with 'a'
print(astring)