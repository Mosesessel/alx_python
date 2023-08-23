#!/usr/bin/python3
def validate_password (password):
    if len(password) < 8:
        return False
    
    # check for uppercase, lowercase, digit and space
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_space = False

    # check for character
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char.isspace():
            has_space = True

    if not (has_uppercase and has_lowercase and has_digit and not has_space):
        return False

    return True                   



