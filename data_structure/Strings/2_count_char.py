"""
@Author: Gyanendra
@Date: 14/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 14/01/2021 
@Title : Strings in Python
"""
import logging
from os import listdir
import sys

def function_length_string(str):
    """
    Description:
        Function is Used for Counting the number of Characters in a sample string 
    Parameter:
        Sample String
    Return:
        Count of Characters
    """
    my_list = list(str)
    temp = set(my_list)
    temp = list(temp)
    count = {}
    for item in temp:
        count[item]= my_list.count(item)
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

    sample_str = "google.com"
    result = function_length_string(sample_str)
    logger.info("Here is the Character frequency of string {} is {} ".format(sample_str, result))
 
  