"""
@Author: Gyanendra
@Date: 14/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 14/01/2021 
@Title : Strings in Python
"""
import logging
import sys

def function_split_char(str, value):
    """
    Description:
        Function is Used to get the last part of a string before a specified character.
    Parameter:
        Sample String 
    Return:
        Updated String before the specified character
    """
    my_list = str.split(value)
    return my_list [0]
             

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

    sample_str = 'https://www.w3resource.com/python-exercises'
    result = function_split_char(sample_str, '-')
    logger.info("Here is the sorted string of {} after replaced specific char is {} ".format(sample_str, result))
