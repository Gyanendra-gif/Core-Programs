"""
@Author: Gyanendra
@Date: 14/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 14/01/2021 
@Title : Tuple in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_repeated_tuple(tup, item):
    """
    Description:
        Function is Used for to check whether an element exists within a tuple and return True or False
    Parameter:
        Sample Tuple
    Return:
        True or False
    """
    if item in tup:
        return True
    else:
        return False

if __name__ == "__main__":
    sample_tuple = (1,2,3,4,5,6,7,2,1)
    result = function_repeated_tuple(sample_tuple, 10)
    logging.debug("The Item in the tuple {} is available {}".format(sample_tuple, result))
  