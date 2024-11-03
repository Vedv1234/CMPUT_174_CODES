# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my number classifier program that collects even
# numbers and identifies odd numbers with special divisibility properties.

# Creating my list for even numbers
even = []

# Checking all numbers from 1 to 100
for number in range(1, 101):
    if number % 2 == 0:  # If I find an even number
        even.append(number)  # Add it to my list
    else:  # For odd numbers
        # Check if it's divisible by 5 or 7
        if number % 5 == 0 or number % 7 == 0:
            print(f" {number} is odd and number is divisible by 5 and 7")

# Calculating the average of my even numbers
average = sum(even) / len(even)
print(f' the average is {average}')