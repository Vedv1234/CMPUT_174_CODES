# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my test file where I'm learning about Python dictionaries.
# I'm trying out different ways to access and modify dictionary data, with comments
# showing what each method does.

# I'm creating a dictionary of student grades for testing
grades = {'Fred': 80, 'Sarah': 98, 'Barney': 99, 'Wilma': 100}

# I tried using get() method for safe access (commented out)
#print(grades.get('Fredd','Error'))

# Method 1: Using items() to get both keys and values
# I can loop through both pieces of data at once
#for key,value in grades.items():
#    print(key,value)
    
# Method 2: Using keys to access values
# This lets me use the key to look up values
#for key in grades.keys():
#    print(key,grades[key])
    
# Method 3: Just getting values
# This only gives me the grades without student names
'''for value in grades.values():
    print(value)'''

# Testing dictionary modification
grades = {'Fred': 80, 'Sarah': 98, 'Barney': 99, 'Wilma': 100}

# I'm trying out the pop method which removes and returns a value
result = grades.pop('Fred')  # This removes Fred and gives me his grade
print(result)

# Notes to myself:
# - pop can use the same error handling as get
# - 'in' operator only checks for keys, not values