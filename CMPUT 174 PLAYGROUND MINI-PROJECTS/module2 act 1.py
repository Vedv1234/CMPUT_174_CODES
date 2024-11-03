# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my protein calculator program that helps me figure out
# how much protein Carol consumed. It converts between different units (kg, pounds, oz)
# and calculates protein content based on a ratio.

# Starting with the total weight in kg
weight_in_kg = 2.32

# I'm calculating Carol's consumption in different units
carol_kg_consumption = 0.333333333 * 2.32  # First converting to kg
carol_pound_consumption = carol_kg_consumption * 2.20462  # Converting to pounds
carol_oz_consumption = carol_pound_consumption * 16  # Converting to ounces

# I'm calculating protein content using the ratio 23/6 and rounding it
carol_protein_consumption = round(carol_oz_consumption * (23/6))

# Displaying my final result
print(f"The grams of protein you consumed is