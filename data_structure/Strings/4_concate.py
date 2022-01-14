"""
@Author: Gyanendra
@Date: 14/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 14/01/2021 
@Title : Strings in Python
"""
import logging
import sys

def function_concate_ing(str):
    """
    Description:
        Function is Used to add 'ing' at the end of a given string (length should be at
        least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length ofconcateging string is less than 3, leave it unchanged. 
    Parameter:
        Sample String
    Return:
        Updated String
    """
    if (len(str) >= 3):
        if str[-3:] == 'ing':
            return str + 'ly'
        else:
            return str + 'ing'            

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

    sample_str = "string"
    result = function_concate_ing(sample_str)
    logger.info("Here is the Replaced Character of {} is {} ".format(sample_str, result))
 
  