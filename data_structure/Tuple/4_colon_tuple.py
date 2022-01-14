"""
@Author: Gyanendra
@Date: 14/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 14/01/2021 
@Title : Tuple in Python
"""
import copy
import logging
logging.basicConfig(level=logging.DEBUG)

def function_colon_tuple():
    """
    Description:
        Function is Used for to create the colon of a tuple.
    Parameter:
        Sample Tuple
    Return:
        None
    """
    sample_tuple = (1,2,[5],6) 
    colon_tuple = copy.deepcopy(sample_tuple)
    colon_tuple[2].append(7)
    logging.debug(sample_tuple)
    logging.debug(colon_tuple)

if __name__ == "__main__":
    function_colon_tuple()
  