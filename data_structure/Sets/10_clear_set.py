"""
@Author: Gyanendra
@Date: 11/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 11/01/2021 
@Title : Set in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_union_set(setOne):
    """
    Description:
        Function is Used for Clear a Set and as a return it will give none
    Parameter:
        Sample Set
    Return:
        None
    """
    result = setOne.clear()
    return result

sample_set_one = {'Black','Blue', 'Green', 'Yellow'}
output = function_union_set(sample_set_one)
logging.debug("Set is Cleared Successfully {} ".format(output))  