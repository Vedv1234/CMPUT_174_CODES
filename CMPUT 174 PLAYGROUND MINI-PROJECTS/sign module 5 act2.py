# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is an extension of my sign-up system where I added
# password matching functionality. Now it checks both username validity and if the
# passwords match.

# I created this function to verify if both entered passwords match
def check_passwords_match(password1, password2):
    if password1 == password2:
        return True
    return False

# My username checker function from before
def check_user_name(name: str, domains: list) -> bool:
    if name.count('@') == 1:
        name_email = name.split('@')
        email_domain = name_email[1]
        if email_domain in domains:
            print('Valid username - proceed to password')
            return True
    print('Invalid username')
    return False

# My main function now handles both username and password checks
def main() -> None:
    # First getting and checking the username
    username = input('Enter user name :')
    domain_list = ['ualberta.ca', 'gmail.com']
    result = check_user_name(username, domain_list)
    
    # If username is valid, I proceed to password checks
    if result:
        # Getting the password twice for verification
        password = input('Enter password :')
        password_again = input('Enter password again :')
        # Checking if passwords match
        match = check_passwords_match(password, password_again)
        if match:
            print('Proceed to Check password strength')

# Running my program
main()