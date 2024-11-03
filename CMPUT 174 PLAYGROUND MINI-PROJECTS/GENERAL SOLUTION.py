# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my math quiz program that generates random
# arithmetic problems for practice. It keeps track of the score and displays
# results in a nicely formatted way.

message = 'MATH IS FUN'
import random

def display_header(string):
    # My function to create nice-looking headers for display
    print(f'+{"-" * (len(string))}+')
    print(f'|{string}|')
    print(f'+{"-" * (len(string))}+')
    
def ask_questions():
    # I'm managing the overall quiz here
    quiz_score = 0
    # Asking 3 questions and keeping track of correct answers
    for index in range(3):
        result = ask_a_question()
        if result:
            quiz_score = quiz_score + 1

def ask_a_question():
    # This is where I generate and check individual math questions
    op = ['+', '-', '*']
    # Getting random numbers and operation
    first = random.randint(1, 10)
    second = random.randint(1, 10)
    op = random.choice(op)
    # Creating the question string
    question = f'{first} {op} {second} = '
    response = int(input(question))
    
    # Calculating the correct answer based on the operation
    if op == '+':
        answer = first + second
    elif op == '-':
        answer = first - second
    else:
        answer = first * second
    
    # Checking if they got it right
    if response == answer:
        print("Correct!")
        return True
    else:
        print("Incorrect!")
    return False
    
def main():
    # My main function that runs the quiz
    display_header(f'{message} - ENDS')
    result = ask_questions()
    print(result)

main()