"""
@Author: Gyanendra
@Date: 14/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 14/01/2021 
@Title : Strings in Python
"""
import logging
import sys

def function_lowercase_string(str, n):
    """
    Description:
        Function is Used to lowercase first n characters in a string.
    Parameter:
        Sample String 
    Return:
        Updated String
    """
    
    my_string = str[:n]
    return my_string.lower() + str[n:]

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

    sample_str = "Welcome to the Bridgelabz Program, Join to get a tech job"
    result = function_lowercase_string(sample_str, 8)
    logger.info("Here is the program of lowercase of string {} is {} ".format(sample_str, result))
