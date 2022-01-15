"""
@Author: Gyanendra
@Date: 14/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 14/01/2021 
@Title : Strings in Python
"""
import logging
import sys

def function_sorted_item(str):
    """
    Description:
        Function is Used to that accepts a comma separated sequence of words as input
        and prints the unique words in sorted form (alphanumerically)..
    Parameter:
        Sample String 
    Return:
        Updated String
    """
    split_list = str.split(',')
    my_list = []
    for item in split_list:
        if item not in my_list:
            my_list.append(item)
    my_list.sort()
    return my_list         

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

    sample_str = 'red, white, black, red, green, black'
    result = function_sorted_item(sample_str)
    logger.info("Here is the sorted string of given string {} is {} ".format(sample_str, result))
 
  