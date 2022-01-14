"""
@Author: Gyanendra
@Date: 14/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 14/01/2021 
@Title : Strings in Python
"""
import logging
import sys

def function_upper_lower(str):
    """
    Description:
        Function is Used to take script that takes input from the user and displays that input back in
        upper and lower cases.
    Parameter:
        Sample String 
    Return:
        Updated String
    """
    upper_format = str.upper()
    lower_format = str.lower()
    return upper_format, lower_format;          

if __name__ == "__main__":

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', 
                              '%m-%d-%Y %H:%M:%S')

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(formatter)

    file_handler = logging.FileHandler('E:\Python Workspace\Core-Programs\data_structure\Strings\string_file.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)

    sample_str = input("Enter the string to get it in upper and lower case: ")
    result = function_upper_lower(sample_str)
    logger.info("Here is the Maximum Length String of List {} is {} ".format(sample_str, result))
 
  