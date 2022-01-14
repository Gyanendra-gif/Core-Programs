"""
@Author: Gyanendra
@Date: 14/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 14/01/2021 
@Title : Tuple in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_remove_tuple(my_list, item):
    """
    Description:
        Function is Used to convert tuple from list 
    Parameter:
        Sample Tuple
    Return:
        Updated Tuple
    """
    my_list = list(sample_tuple)
    my_list.remove(item)
    return tuple(my_list)

if __name__ == "__main__":
    sample_tuple = (1,2,3,4,5,6,7)
    result = function_remove_tuple(sample_tuple, 4)
    logging.debug("The Item from the tuple {} is removed {}".format(sample_tuple, result))
