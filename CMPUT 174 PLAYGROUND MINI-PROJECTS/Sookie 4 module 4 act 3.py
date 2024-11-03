# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: I created this program to calculate employee salaries and find who worked 
# above average hours. It helped me practice file handling and list operations in Python.

# Setting up my payment details
pay_rate = 20  # Pay rate per hour

# Opening my employee file to read the data
filename = 'employees.txt'
mode = 'r'
with open(filename, mode) as file:
    list_of_lines = file.readlines()  # Reading all lines from my file

# Creating lists to store my employee data
total_hours = []  # To store total hours for each employee
names = []        # To store employee names

# Processing each line from my file
for line in list_of_lines:
    line = line.strip()  # Removing extra whitespace
    record = line.split()  # Splitting line into list of values
    print(record)  # Printing the current record
    
    # Getting employee name and calculating their hours
    name = record[0]  # First item is the name
    hours = 0
    for index in range(1, len(record)):  # Adding up all their hours
        hours = hours + int(record[index])
    
    # Storing the data and calculating salary
    names.append(name)
    total_hours.append(hours)
    salary = hours * pay_rate
    print(f'{name} earned {hours} hours so her salary is: ${salary}')

# Calculating average hours worked
average = sum(total_hours)/len(total_hours)    

# Printing my lists for verification
print(names)
print(total_hours)

# Finding who worked above average hours
above_average = []
for index in range(len(names)):
    if total_hours[index] > average:
        above_average.append(names[index])

# Creating final output string
above_average_str = ','.join(above_average)
print(above_average_str)
print(f'{above_average_str} worked more than {average} hours.')