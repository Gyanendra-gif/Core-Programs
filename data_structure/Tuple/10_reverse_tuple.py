"""
@Author: Gyanendra
@Date: 14/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 14/01/2021 
@Title : Tuple in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_reverse_tuple(tup):
    """
    Description:
        Function is Used for reverse a tuple is added
    Parameter:
        Sample Tuple
    Return:
        Updated Tuple 
    """
    reverse_tuple = tup[::-1]
    return tuple(reverse_tuple)

if __name__ == "__main__":
    sample_tuple = (1,2,3,6,5,6,7)
    result = function_reverse_tuple(sample_tuple)
    logging.debug("The Reversed tuple from the tuple {} is {}".format(sample_tuple, result))
