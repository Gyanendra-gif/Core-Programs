"""
@Author: Gyanendra
@Date: 16/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 16/01/2021 
@Title : User Registration in Python
"""

import re
from logging_config import logger

def function_name_validate(name):
    """
    Description:
        Function is Used for Validating the First Name of User and will record the data on
        log file
    Parameter:
        Sample String as Name
    Return:
        None
    """
    pattern = r'^[a-zA-Z]{3,30}$'
    match = re.fullmatch(pattern, name)
    if match:
        logger.info('First Name is Valid')
    else:
        logger.error('Error! First Name is Not Valid')

if __name__ == "__main__":
    user_name = input("Enter Your First Name to Check Validation: ")
    function_name_validate(user_name)        