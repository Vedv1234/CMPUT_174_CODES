# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: I wrote this program to understand what type of value
# the print function returns. It helped me learn about function return types.

# I commented out this test print
#print('hello')

# My function to test what print() returns
def testing():
    # I'm printing hello and then checking its return type
    # This will show me that print() returns None
    print(type(print('hello')))
    
# Running my test function    
testing()