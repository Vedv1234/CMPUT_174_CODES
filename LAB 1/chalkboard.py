# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: I made this program to recreate Bart Simpson's chalkboard punishment scenes! 
# It takes a phrase from the user and repeats it as many times as they want - just like Bart 
# writing lines on the chalkboard. Pretty fun way to practice basic input and string multiplication!

# I'm asking the user what phrase they want Bart to write
phrase_entered = input(" Please enter the phrase which is to be repeated: ")

# Now I need to know how many times they want to torture Bart with writing it
iterations = int(input(" Please enter the number of times the phrase is to be repeated: "))

# Here's where the magic happens - I multiply the phrase by the number of times we want it repeated
display_text = phrase_entered * iterations

# Finally, I show the user all those repeated lines, just like on Bart's chalkboard
print(display_text)