# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: I built this temperature converter to help our Canadian viewers 
# understand Springfield's weather! It takes a temperature in Celsius (because that's what 
# we use in Canada) and converts it to Fahrenheit (which is what they use in Springfield). 
# Added a D'oh! at the end because, well, it's The Simpsons!

# First, I'm getting the temperature in Celsius from the user
temperature_in_celcius = float(input("Kindly enter the temperature in Degrees Celcius: "))

# Here's where I do the conversion - multiplying by 9/5 and adding 32
# I used round() to keep the numbers clean
temperature_in_fahrenheit = round(temperature_in_celcius * 9/5) + 32

# Finally, I'm showing both temperatures with a little Simpsons flair!
print(f"{temperature_in_celcius} degrees in Canada would be {temperature_in_fahrenheit} degrees in Springfield. D'oh!")