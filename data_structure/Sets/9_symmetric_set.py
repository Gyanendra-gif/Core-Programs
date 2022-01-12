"""
@Author: Gyanendra
@Date: 11/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 11/01/2021 
@Title : Set in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_union_set(setOne, setTwo):
    """
    Description:
        Function is Used for Symmetric Difference of two Sets and it will return all
        elements except common one
    Parameter:
        Sample Set
    Return:
        Updated Set
    """
    result = setOne.symmetric_difference(setTwo)
    return result

sample_set_one = {'Black','Blue', 'Green', 'Yellow'}
sample_set_two = {'Red', 'Pink', 'Orange', 'Blue','Black'}
output = function_union_set(sample_set_one,sample_set_two)
logging.debug("Here is the Updated Set is {} ".format(output))  