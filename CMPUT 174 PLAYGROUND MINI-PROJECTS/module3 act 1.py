# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my temperature checker program for Mr. Ratburn.
# It helps determine if students need to wear jackets based on the temperature.

# Getting temperature input from Mr. Ratburn
TempCelcius = int(input("Please enter Temperature in Celcius Mr.Ratburn:"))

# I'm checking if it's cold enough to require jackets
if TempCelcius < 0:
    print("Students need to wear jacket")