# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my quiz mark adjuster that modifies quiz scores
# based on participation levels. Different participation grades give different
# percentage increases to the final mark.

# Getting initial quiz mark and participation level
quiz_mark = float(input('Enter quiz mark > '))
changed = False  # I'm using this flag to track if I modified the mark
percent_increase = 0
participation_level = input('Enter particiaption level: A,S,U,R,N:')

# I'm determining the percentage increase based on participation
if participation_level == 'A':
    percent_increase = 0.2    # 20% increase for 'A' participation
elif participation_level == 'U':
    percent_increase = 0.15   # 15% for 'U'
elif participation_level == 'S':
    percent_increase = 0.10   # 10% for 'S'
elif participation_level == 'R':
    percent_increase = 0.05   # 5% for 'R'
else:
    percent_increase = 0      # No increase for 'N' or invalid inputs

import math

# I'm applying the increase if there is one
if percent_increase != 0:
    quiz_mark = round(quiz_mark + (quiz_mark * percent_increase))
    changed = True

# Showing the results
if changed:
    print(f"New quiz mark is : {quiz_mark}")
else:
    print('Quiz mark remains unchanged')