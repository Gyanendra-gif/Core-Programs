"""
@Author: Gyanendra
@Date: 14/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 14/01/2021 
@Title : Strings in Python
"""
import logging
import sys

def function_reversed_string(str):
    """
    Description:
        Function is Used to reverse a string.
    Parameter:
        Sample String 
    Return:
        Reversed String
    """
    data = ' '
    my_string = len(str)
    for i in range (my_string).__reversed__():
        data = data + str[i]
    return data

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
    result = function_reversed_string(sample_str)
    logger.info("Here is the count of occurence in {} of sub string is {} ".format(sample_str, result))
 
  