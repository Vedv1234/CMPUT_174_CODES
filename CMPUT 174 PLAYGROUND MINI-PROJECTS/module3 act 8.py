# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my number analyzer program that works with numbers
# from 1 to 100. It collects even numbers divisible by both 5 and 7, and identifies
# odd numbers divisible by either 5 or 7.

# I'm creating an empty list to store my even numbers
even = []

# Looking through all numbers from 1 to 100
for number in range(1, 101):
    if number % 2 == 0:  # If it's even
        # I only add it if it's divisible by both 5 and 7
        if number % 5 == 0 and number % 7 == 0:
            even.append(number)
    else:  # If it's odd
        # I print it if it's divisible by either 5 or 7
        if number % 5 == 0 or number % 7 == 0:
            print(f" {number} is divisible by 5 or 7")

# Calculating and displaying the average of my collected even numbers
average = sum(even)/len(even)
print(f"{average} is the average of the even numbers.")