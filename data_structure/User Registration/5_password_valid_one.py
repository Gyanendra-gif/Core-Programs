"""
@Author: Gyanendra
@Date: 16/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 16/01/2021 
@Title : User Registration in Python
"""

import re
from logging_config import logger

def function_password_validate(password):
    """
    Description:
        Function is Used for Validating the Password of User 
    Parameter:
        Sample String
    Return:
        None
    """
    pattern = r'(.{8,})+'
    match = re.fullmatch(pattern, password)
    if match:
        logger.info('Entered Password is Valid')
    else:
        logger.error('Error! Entered Password is Not Valid')

if __name__ == "__main__":
    user_input = input('Enter Password atleast having eight characters to check validation: ')
    function_password_validate(user_input)        