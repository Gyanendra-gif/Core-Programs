"""
@Author: Gyanendra
@Date: 16/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 16/01/2021 
@Title : User Registration in Python
"""
import re

def function_email_validate(str):
    """
    Description:
        Function is Used for Validating the Email Address of User 
    Parameter:
        Sample String
    Return:
        None
    """
    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{1,63}$'
    match = re.fullmatch(pattern, str)
    if match:
        return True
    else:
        return False

def function_password_validate(str):
    """
    Description:
        Function is Used for Validating the Password of User with having Eight Characters and one
        Upper case letter and having one numeric character also with one special char
    Parameter:
        Sample String
    Return:
        None
    """
    pattern = r'(?=.*[A-Z])(?=.*[0-9])(?=.*[@!#$%^&*_-]).{8,}'
    match = re.fullmatch(pattern, str)
    if match:
        return True
    else:
        return False        