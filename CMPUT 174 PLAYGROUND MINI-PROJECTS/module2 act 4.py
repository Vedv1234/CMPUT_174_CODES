# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my exercise instruction parser. It takes a coded
# exercise string (like "3x12,60") and breaks it down into sets, reps, and rest time
# to create a readable instruction.

# Getting the exercise code from user
exercise_code = input('Enter exercise code >')

# I'm finding the positions of special characters to help split the code
x_position = exercise_code.find('x')
comma_position = exercise_code.find(',')

# Using string slicing to extract each part:
sets = exercise_code[0:x_position]  # Everything before 'x'
reps = exercise_code[x_position+1:comma_position]  # Between 'x' and ','
rest_time = exercise_code[comma_position+1:len(exercise_code)]  # Everything after ','

# Creating my formatted instruction message
print(f" Perform {sets} sets of bench press at {reps} reps each. Rest for {rest_time} secs between each set")