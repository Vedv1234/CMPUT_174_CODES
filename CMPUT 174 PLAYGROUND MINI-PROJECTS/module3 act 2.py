# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my classroom seating program. It assigns students
# to either the left or right side of the room based on the first letter of their
# name (A-M go left, N-Z go right).

# Getting the student's name and converting to uppercase
student_name = (input("Enter name of student:")).upper()

# I'm checking the first letter to decide which side they should sit on
if student_name[0] >= 'A' and student_name[0] <= 'M':
    print('Left side')
else:
    print('Right side')