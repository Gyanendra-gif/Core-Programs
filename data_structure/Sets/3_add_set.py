"""
@Author: Gyanendra
@Date: 11/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 11/01/2021 
@Title : Dictionary in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_add_set(set):
    """
    Description:
        Function is Used for Adding Items in set
    Parameter:
        Sample Set
    Return:
        None
    """
    user_input = input("Enter the Name to add in set ")
    result = set.add(user_input)
    return result

sample_set = {'Sam', 'Tom', 'Harry'}
output = function_add_set(sample_set)
logging.debug("Here is the Updated Set is {} ".format(sample_set ,output))   