# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my grade calculator program. It takes a numerical
# mark as input and converts it to a letter grade using standard grade boundaries.

# Getting the mark from user
mark = float(input('Enter mark: '))

# I'm using if-elif statements to determine the grade
if mark < 0 or mark > 100:
    print('Invalid mark')
elif mark >= 0 and mark <= 50:
    print("GRADE F")
elif mark > 50 and mark <= 60:
    print("GRADE D")
elif mark > 60 and mark <= 70:
    print("GRADE C")
elif mark > 70 and mark <= 80:
    print("GRADE B")
else:
    print("GRADE A")