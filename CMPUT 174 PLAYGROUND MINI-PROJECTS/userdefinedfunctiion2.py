# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: I created this program to simulate a coffee machine that checks
# water levels before making coffee. It helped me understand function parameters and return values.

# My function to check if there's enough water
def check_water_leve(level):  # Note: There's a typo in function name
    if level > 2:
        return True
    else:
        return False

# My function to make coffee based on type and water level
def make_coffee(type_of_coffee, level):
    # Bug: I misspelled the function name in the call
    if check_water_level(level):  # This will cause an error due to misspelling above
        print(f'Here is your delicious cup of {type_of_coffee} coffee')
    else:
        print(f'Error Insufficient water level')

# Getting input from the user
user_input = input('Type of Coffee >')
water_level = input('Enter Water level')  # Bug: Need to convert this to int
    
# Making coffee with user's choices
make_coffee(user_input, water_level)  # Passing 2 arguments to my function