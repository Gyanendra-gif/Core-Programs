"""
@Author: Gyanendra
@Date: 12/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 12/01/2021 
@Title : List in Python
"""
import logging
from itertools import permutations
logging.basicConfig(level=logging.DEBUG)

def function_permutation_list(lst):
    """
    Description:
        Function is Used for calculating permutation of list
    Parameter:
        Sample List
    Return:
        Sorted List
    """
    updated_list = permutations(lst)
    return list(updated_list)
    
if __name__ == "__main__":
    sample_list = [1,2,3]
    result = function_permutation_list(sample_list)
    logging.debug("List of all permutations from {} is {}".format(sample_list, result))
