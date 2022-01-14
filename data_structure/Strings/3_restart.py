"""
@Author: Gyanendra
@Date: 14/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 14/01/2021 
@Title : Strings in Python
"""
import logging
import sys

def function_replace_char(str):
    """
    Description:
        Function is Used to get a string from a given string where all occurrences of its
        first char have been changed to '$', except the first char itself. 
    Parameter:
        Sample String
    Return:
        Updated String
    """
    my_list = list(str)
    for i in range(1, len(my_list)):
        if my_list[i] == my_list[0]:
            my_list[i] = '$'
    data = ' '
    for item in my_list:
        data = data + item   
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

    sample_str = "restart"
    result = function_replace_char(sample_str)
    logger.info("Here is the Replaced Character of string {} is {} ".format(sample_str, result))
 
  