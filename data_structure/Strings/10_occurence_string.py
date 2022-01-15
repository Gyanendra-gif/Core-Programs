"""
@Author: Gyanendra
@Date: 14/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 14/01/2021 
@Title : Strings in Python
"""
from itertools import count
import logging
import sys
import textwrap
from turtle import st

def function_occurence_string(str, substr):
    """
    Description:
        Function is Used to get the display formatted text (width=50) as output.
    Parameter:
        Sample String 
    Return:
        Updated String
    """
    count = str.count(substr)
    return count

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
    sample_sub_str = "to"
    result = function_occurence_string(sample_str, sample_sub_str)
    logger.info("Here is the count of occurence in {} of sub string is {} ".format(sample_str, result))
 
  