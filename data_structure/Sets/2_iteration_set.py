"""
@Author: Gyanendra
@Date: 11/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 11/01/2021 
@Title : Dictionary in Python
"""
import logging
logging.basicConfig(level=logging.INFO)

def function_iterate_set(set):
    """
    Description:
        Function is Used for Iterating Set
    Parameter:
        Sample Set
    Return:
        None
    """
    for value in set:
        logging.info(value)
        
sample_set = {1,2,3,4,5,6,7,8,9,10}
result = function_iterate_set(sample_set)
      