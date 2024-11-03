# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is another version of my employee salary calculator
# that handles corrupted files. I made some small improvements to the output formatting.

# Setting up my constants
pay_rate = 20
filename = 'employees_Corrupted.txt'
mode = 'r'

# Creating my lists for storing employee data
total_hours = []
names = []

# Reading my file
with open(filename, mode) as file:
    list_of_lines = file.readlines()
    
# Processing each line of my file
for line in list_of_lines:
    line = line.strip()
    if len(line) != 0:  # Skipping empty lines
        record = line.split()
        name = record[0]
        hours = 0
        # Calculating total hours for this employee
        for index in range(1, len(record)):
            hours = hours + int(record[index])
        # Storing the data
        total_hours.append(hours)
        names.append(name)
        salary = hours * pay_rate
        print(f" {name} {hours} ${salary}")
    
# Printing my collected data
print(names)
print(total_hours)

# Finding my above-average workers
average = sum(total_hours) / len(total_hours)
above_average = []
for index in range(len(names)):
    if total_hours[index] > average:
        above_average.append(names[index])

# Printing my final results
print(above_average)
above_average_str = ','.join(above_average)
print(f"the average amount of hours worked by all employees is {average}.")
print(f"{above_average_str} worked more than {average} hours per week")