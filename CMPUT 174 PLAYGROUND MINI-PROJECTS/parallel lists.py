# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my grade analyzer program that works with parallel
# lists - one for names and one for grades. It identifies students who scored
# above 80.

# My lists for student data
names = ['Sarah', 'Bob', 'Alice']
grades = [70, 85, 90]

# I'm trying to find students with grades above 80
# Note: There seems to be some errors in the original code, here's how I'd fix it:

count = 0  # I need to initialize my counter
for i in range(len(names)):  # Using index to match names with grades
    if grades[i] > 80:
        print(f" {names[i]} achieved a grade above 80")
        count = count + 1
    
print(f" number of students who got grades above 80 are {count}")