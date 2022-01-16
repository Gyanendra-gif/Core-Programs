"""
@Author: Gyanendra
@Date: 16/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 16/01/2021 
@Title : User Registration in Python
"""

import re
from logging_config import logger

def function_email_validate(mail):
    """
    Description:
        Function is Used for Validating the Email Address of User 
    Parameter:
        Sample String as Name
    Return:
        None
    """
    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{1,63}$'
    match = re.fullmatch(pattern, mail)
    if match:
        logger.info('Email Address is Valid')
    else:
        logger.error('Error! Email Address is Not Valid')

if __name__ == "__main__":
    user_input = input("Enter Email Address to Check Validation: ")
    function_email_validate(user_input)        