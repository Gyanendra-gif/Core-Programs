"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 11/01/2021 
@Title : Dictionary in Python
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

sample_list = ["Tom", "Harry", "Sam"]
result = function_create_set(sample_list)
logging.debug("Created Sample Set is {}".format(sample_list, result))
  