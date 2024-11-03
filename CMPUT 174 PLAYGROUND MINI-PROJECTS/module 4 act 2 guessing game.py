# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my jelly bean guessing game where players get three
# attempts to guess a number. I give different hints after wrong guesses and award
# different scores based on how quickly they get it right.

# Setting up my game constants
jelly_beans = '2014'  # I'm using a string to make it easier to show hints
max_attempts = 3

# Initializing my game variables
user_attempt = 0
guess = ''  # Starting with empty guess

# My game loop runs until either:
# 1. Player guesses correctly, or
# 2. They run out of attempts
while guess != jelly_beans and user_attempt < max_attempts:
    guess = input('Enter guess > ')
    user_attempt = user_attempt + 1
    
    if guess != jelly_beans:  # They got it wrong
        # I'm giving different hints based on which attempt they're on
        if user_attempt == 1:
            # First hint: sum of all digits
            total = 0
            for digit in jelly_beans:
                total = total + int(digit)
            print(f'HINT1 : {total}')
        elif user_attempt == 2:
            # Second hint: first and last digits
            first_digit = jelly_beans[0]
            last_digit = jelly_beans[-1]
            print(f'HINT2: {first_digit},{last_digit}')
        else:
            # No more hints on last attempt
            print('Better Luck next time')
    else:  # They got it right!
        # I give different scores based on how many attempts they took
        if user_attempt == 1:
            print('50%')
        elif user_attempt == 2:
            print('25%')
        else:
            print('10%')