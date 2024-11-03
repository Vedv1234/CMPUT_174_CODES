# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my matrix handler program that reads matrix data
# from a file and displays it in different formats. I'm learning how to work with
# 2D lists and format output nicely.

def build_matrix(filename):
    # I'm reading and building my matrix from a file
    with open(filename, 'r') as file:
        alist = file.readlines()
        # First two lines tell me the size
        rows = int(alist[0].strip())
        columns = int(alist[1].strip())
        
        # Creating my empty matrix
        matrix = []
        index = 2  # Data starts from third line
        
        # Building the matrix row by row
        for row_index in range(rows):
            a_row = []
            for col_index in range(columns):
                item = int(alist[index].strip())
                index = index + 1
                a_row.append(item)
            matrix.append(a_row)
        return(matrix)

def display_matrix_1(matrix):
    # This is my first way to display the matrix - using row iteration
    for row in matrix:
        a_row = ' '
        for element in row:
            # I'm using format specifiers to make it look neat
            a_row = (f" {a_row} {element:8} ")
        print(a_row)

def display_matrix_2(matrix):
    # This is my second way - using indices
    rows = len(matrix)
    cols = len(matrix[0])
    for row_index in range(rows):
        a_row = ' '
        for col_index in range(cols):
            a_row += str(matrix[row_index][col_index]) + ' '
        print(a_row)

def main():
    # Testing both my display methods
    filename = 'matrix.txt'
    matrix = build_matrix(filename)
    print(" Displaying matrix by accessing the elements directly")
    display_matrix_1(matrix)
    print(" Displaying matrix by accessing the indices of the elements")
    display_matrix_2(matrix)

main()