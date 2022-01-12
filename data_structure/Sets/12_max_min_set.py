"""
@Author: Gyanendra
@Date: 11/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 11/01/2021 
@Title : Set in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_max_set(setOne):
    """
    Description:
        Function is Used for finding max value of Set
    Parameter:
        Sample Set
    Return:
        Updated Set
    """
    result = max(setOne)
    return result

def function_min_set(setOne):
    """
    Description:
        Function is Used for finding min value of Set
    Parameter:
        Sample Set
    Return:
        Updated Set
    """
    result = min(setOne)
    return result    

sample_set_one = {23,45,65,12,87,96,2,4}
max_value = function_max_set(sample_set_one)
min_value = function_min_set(sample_set_one)
logging.debug("Here is the Max Value of Set is {} ".format(max_value)) 
logging.debug("Here is the Min Value of Set is {} ".format(min_value)) 
