"""
@Author: Gyanendra
@Date: 11/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 11/01/2021 
@Title : Set in Python
"""
import logging
from typing import FrozenSet
logging.basicConfig(level=logging.DEBUG)

def function_union_set(setOne):
    """
    Description:
        Function is Used for Create a Frozen Set of a set
    Parameter:
        Sample Set
    Return:
        Updated Set
    """
    result = frozenset(setOne)
    return result

sample_set_one = {'Black','Blue', 'Green', 'Yellow'}
output = function_union_set(sample_set_one)
logging.debug("Here is the Frozen Set is {} ".format(output))  