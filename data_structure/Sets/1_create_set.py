"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 11/01/2021 
@Title : Sets in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_create_set(list):
    """
    Description:
        Function is Used for Creating Sample Set
    Parameter:
        Sample List
    Return:
        Created Set
    """
    sample_set = set(list)
    return sample_set

demo_set = {"Tom", "Harry", "Sam"}
result = function_create_set(demo_set)
logging.debug("Created Sample Set is {}".format(demo_set, result))
 
  