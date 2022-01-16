"""
@Author: Gyanendra
@Date: 16/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 16/01/2021 
@Title : User Registration in Python
"""

import re
from logging_config import logger

def function_mobile_validate(mobile_num):
    """
    Description:
        Function is Used for Validating the Mobile Number of User 
    Parameter:
        Sample String as Number
    Return:
        None
    """
    pattern = r'([0-9]{2,})+(\s[0-9]{10})+'
    match = re.fullmatch(pattern, mobile_num)
    if match:
        logger.info('Mobile Number is Valid')
    else:
        logger.error('Error! Mobile Number is Not Valid')

if __name__ == "__main__":
    user_input = input('Enter Mobile Number to Check Validation: ')
    function_mobile_validate(user_input)        