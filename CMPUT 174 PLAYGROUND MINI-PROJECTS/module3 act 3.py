# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my class reward program that helps me decide what
# treats to bring based on the class average. Higher averages get better treats!

# Getting the class average from input
average = int(input("Enter the class average:"))

# I'm using if-elif-else to decide which treat to bring
if average <= 40:
    print("bring lollipops")  # My basic treat for low scores
elif average <= 90:
    print("Bring cookies")    # Better treat for good scores
else:
    print("Bring Ice-cream")  # Best treat for excellent scores!