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
        Function is Used to that takes a list of words and returns the length of the longest one.
    Parameter:
        Sample String in List Form
    Return:
        Updated String
    """
    my_list = []
    for i in str:
        my_list.append(len(i))
    result_index = my_list.index(max(my_list))
    return str[result_index]           

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

    sample_str = ['Gyanendra', 'Bridgelabz', 'Sam']
    result = function_concate_ing(sample_str)
    logger.info("Here is the Maximum Length String of List {} is {} ".format(sample_str, result))
 
  