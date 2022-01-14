"""
@Author: Gyanendra
@Date: 14/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 14/01/2021 
@Title : Tuple in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_list_tuple(list):
    """
    Description:
        Function is Used for to check whether an element exists within a tuple and return True or False
    Parameter:
        Sample Tuple
    Return:
        True or False
    """
    my_tuple = tuple(list)
    return my_tuple

if __name__ == "__main__":
    sample_list = [1,2,3,4,5,6,7]
    result = function_list_tuple(sample_list)
    logging.debug("The Item in the List {} is Converted to tuple {}".format(sample_list, result))
  