# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my grade calculator that converts numerical marks
# into letter grades. It also checks if the mark is valid (between 0 and 100).

# Getting the student's mark
mark = int(input("Please enter student mark:"))

# I'm first checking if the mark is in a valid range
if mark > 0 and mark < 100:
    # Then I'm using nested if statements to determine the grade
    if mark >= 0 and mark <= 50:
        print("Grade is F")
    elif mark > 50 and mark <= 60:
        print("Grade is D")
    elif mark > 60 and mark <= 70:
        print("Grade is C")
    elif mark > 70 and mark <= 80:
        print("Grade is B")
    else:
        print("Grade is A")
else:
    print("Number invalid")