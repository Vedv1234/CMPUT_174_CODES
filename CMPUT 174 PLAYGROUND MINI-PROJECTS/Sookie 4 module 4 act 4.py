# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: I improved my previous employee salary program to handle corrupted files 
# with random whitespace. This helped me understand file handling with messy data.

# Setting my payment rate
pay_rate = 20

# Opening my corrupted employee file
filename = 'employees_c.txt'
mode = 'r'
with open(filename, mode) as file:
    list_of_lines = file.readlines()

# Creating my lists to store employee data
total_hours = []
names = []

# Processing each line, now with extra checks for corrupted data
for line in list_of_lines:
    line = line.strip()  # Removing extra whitespace
    if len(line) != 0:   # Only processing non-empty lines
        record = line.split()  # Splitting on whitespace handles multiple spaces
        name = record[0]
        hours = 0
        # Adding up all hours for this employee
        for index in range(1, len(record)):
            hours = hours + int(record[index])
        
        # Storing the data and calculating salary
        names.append(name)
        total_hours.append(hours)
        salary = hours * pay_rate
        print(f'{name} {hours} ${salary}')

# Calculating and finding above-average workers
average = sum(total_hours)/len(total_hours)    
print(names)
print(total_hours)

# Making my list of above-average workers
above_average = []
for index in range(len(names)):
    if total_hours[index] > average:
        above_average.append(names[index])

# Creating and printing my final output
above_average_str = ','.join(above_average)
print(above_average_str)
print(f'{above_average_str} worked more than {average} hours.')