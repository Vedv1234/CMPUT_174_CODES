# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is the final version of my sign-up system where I added
# complete password validation. It checks for length, digits, capital letters, and
# special characters in the password.

# My function to check if password has at least one special character
def check_password_special(password: str) -> bool:
    for char in password:
        # isalnum() returns False for special characters
        if not char.isalnum():
            return True
    print('Missing special character !')
    return False

# My function to check if password has at least one capital letter
def check_password_capital(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    print('Missing capital letter !')
    return False

# My function to check if password has at least one digit
def check_password_digit(password: str) -> bool:
    for char in password:
        if char.isdigit():
            return True
    print('Missing digit !')
    return False

# My function to check if password meets minimum length requirement
def check_password_len(password: str, length: int) -> bool:
    if len(password) >= length:
        return True
    return False

# My password matching function from before
def check_passwords_match(password1, password2):
    if password1 == password2:
        return True
    return False

# My username checking function from before
def check_user_name(name: str, domains: list) -> bool:
    if name.count('@') == 1:
        name_email = name.split('@')
        email_domain = name_email[1]
        if email_domain in domains:
            print('Valid username - proceed to password')
            return True
    print('Invalid username')
    return False

# My main function now includes all password validation checks
def main() -> None:
    username = input('Enter user name :')
    domain_list = ['ualberta.ca', 'gmail.com']
    required_length = 8
    
    # First checking username
    result = check_user_name(username, domain_list)
    if result:
        # If username is valid, getting and checking password
        password = input('Enter password :')
        password_again = input('Enter password again :')
        match = check_passwords_match(password, password_again)
        
        # If passwords match, I run all my password validation checks
        if match:
            has_length = check_password_len(password, required_length)
            has_digit = check_password_digit(password)
            has_capital = check_password_capital(password)
            has_special = check_password_special(password)
            
            # If all password requirements are met, registration is complete
            if has_length and has_digit and has_capital and has_special:
                print('Registered')

# Running my program
main()