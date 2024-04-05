import re

def validate_password(password):
    UPPER_REGEX = re.compile(r'[A-Z]')
    LOWER_REGEX = re.compile(r'[a-z]')
    DIGIT_REGEX = re.compile(r'[0-9]')
    SPECIAL_REGEX = re.compile(r'[!@#\$%\^&\*.,?\[\]\(\)\{\}]')

    # password too short
    if len(password) < 8:
        return False
    
    # no uppercase letter
    if not UPPER_REGEX.search(password):
        return False
    
    # no lowercase letter
    if not LOWER_REGEX.search(password):
        return False
    
    # no digit
    if not DIGIT_REGEX.search(password):
        return False
    
    # no special character
    if not SPECIAL_REGEX.search(password):
        return False
    
    return True