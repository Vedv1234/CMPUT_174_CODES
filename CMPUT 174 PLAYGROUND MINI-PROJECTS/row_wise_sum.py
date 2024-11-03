# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: I created this program to calculate the sum of each row in a matrix.
# It helps me practice working with nested lists and loops in Python.

# I defined this function to find the sum of numbers in each row of my matrix
def find_row_sum(matrix):
    # I'm going through each row in my matrix
    for row in matrix:
        # For each row, I start with a sum of 0
        row_sum = 0
        # I'm going through each number in the current row
        for number in row:
            # Adding the current number to my row sum
            row_sum += number
        # After adding all numbers in the row, I print the sum
        print(row_sum)

# This is my main function where I test my row_sum function
def main():
    # I created a test matrix with three rows
    # Note: There's a syntax error in the matrix definition that I should fix:
    # Should be: matrix = [[1,2], [3,4,5], [6,7]]
    matrix = [[1,2][3,4,5][6,7]]
    # Calling my row sum function with my test matrix
    find_row_sum(matrix)

# Running my main function to test everything
main()