'''
Create functions for validate_user and register_user using provided functions: validate_name, validate_email, validate_password
'''

def validate_user(name, email, password):
    """Checks that the data input by the user is in the valid format.
    
    Args:
        name (str): The inputted name from the user.
        email (str): The inputted email from the user.
        password (str): The inputted password from the user.
        
    Returns:
        bool: True if the input passes all validation checks, raises a ValueError otherwise.
    """
    if not(validate_name(name)):
        raise ValueError('Input name not in valid format')
    if not(validate_email(email)):
         raise ValueError('Input email not in valid format')
    if not(validate_password(password)):
         raise ValueError('Input password not in valid format')
    return True

def register_user(name, email, password):
    """Registers a new user.
    
    Args:
        name (str): The inputted name from the user.
        email (str): The inputted email from the user.
        password (str): The inputted password from the user.
        
    Returns:
        dict: Returns a dictionary with user input details if new user
        bool: Returns False if user already exists
    """
    if not (validate_user(name, email, password)):
        return False
    return {'name': name, 'email': email, 'password': password}

name = 'James'
password = 'Jamesewok675'
email = 'james@sibes.com'
print("Is the user valid?\n",validate_user(name, email, password))
print(register_user(name, email, password))