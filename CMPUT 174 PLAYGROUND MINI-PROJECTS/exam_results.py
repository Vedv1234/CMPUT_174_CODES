# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my program to process multiple-choice exam results.
# It handles different versions of the exam (111, 333, 555, 777), reads student responses
# and answer keys from files, and generates a formatted report showing how each student did.

'''[Original problem description kept as is for reference]'''

def read_responses(filename) -> (dict, dict):
    # I'm creating two dictionaries here to store student data
    names_versions = {}  # I'll store which version each student took
    names_responses = {}  # I'll store their actual answers
    with open(filename, 'r') as file:
        for line in file:
            # I'm processing each line to extract student info
            line = line.strip()
            record = line.split()
            name = record[0]
            version = record[1]
            responses = record[2:]
            # Storing the data in my dictionaries
            names_versions[name] = version
            names_responses[name] = responses
    return names_versions, names_responses
    
def read_keys(filename):
    # I'm reading the answer keys for each version
    versions_answers = {}
    with open(filename, 'r') as file:
        for line in file:
            # Processing each line to get version and its answers
            line = line.strip()
            record = line.split()
            version = record[0]
            answers = record[1:]
            versions_answers[version] = answers
    return versions_answers

def match_answers(names_versions, names_responses, versions_answers):
    # This is where I check student answers against the keys
    names_scores = {}
    for name, responses in names_responses.items():
        correct = 0
        version = names_versions[name]
        answers = versions_answers[version]
        # Counting how many answers they got right
        for index in range(len(answers)):
            if answers[index] == responses[index]:
                correct = correct + 1
        names_scores[name] = correct
    return names_scores

def display_header(string):
    # My helper function to create formatted headers
    print(f'+{"-" *len(string)}+')
    print(f'|{string}|')
    print(f'+{"-" *len(string)}+')
    
def display_results(names_responses, names_versions, versions_answers, names_scores):
    # This is my main display function that shows the formatted report
    for version, answers in versions_answers.items():
        # Creating header for each version
        string = f'Version {version} Key:{" ".join(answers)}'
        display_header(string)
        # Showing results for students who took this version
        for name, responses in names_responses.items():
            s_version = names_versions[name]
            if s_version == version:
                score = names_scores[name]
                total = len(responses)
                print(f'{name} {" ".join(responses)} {score}/{total}')

def main():
    # My main function that brings everything together
    filename1 = 'responses.txt'
    filename2 = 'keys.txt'
    # Reading files and processing data
    names_versions, names_responses = read_responses(filename1)
    versions_answers = read_keys(filename2)
    names_scores = match_answers(names_versions, names_responses, versions_answers)
    # Displaying the final report
    display_results(names_responses, names_versions, versions_answers, names_scores)

if __name__ == '__main__':
    main()