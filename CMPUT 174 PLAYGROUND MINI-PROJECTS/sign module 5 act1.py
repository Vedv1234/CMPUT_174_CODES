# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: In this program, I'm creating a username validator that checks
# if an email address has exactly one @ symbol and belongs to allowed domains.
# This is part of my sign-up system project.

# I'm implementing a function to check if the username (email) is valid
# Using type hints to make my code more readable and catch potential errors
def check_user_name(name: str, domains: list) -> bool:
    # First I check if there's exactly one @ symbol
    if name.count('@') == 1:
        # I split the email into username and domain parts
        name_email = name.split('@')
        # Getting the domain part (after @)
        email_domain = name_email[1]
        # Checking if the domain is in my allowed list
        if email_domain in domains:
            # If everything is valid, I print a success message
            print('Valid username - proceed to password')
            return True
    # If any check fails, I print an error message
    print('Invalid username')
    return False

# My main function to test the username checker
def main() -> None:
    # Getting the username from user input
    username = input('Enter user name :')
    # My list of allowed domains
    domain_list = ['ualberta.ca', 'gmail.com']
    # Testing the username against my checker
    check_user_name(username, domain_list)

# Running my program
main()