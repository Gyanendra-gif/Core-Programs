"""
@Author: Gyanendra
@Date: 12/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 12/01/2021 
@Title : List in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_duplicate_list(list):
    """
    Description:
        Function is Used for remove duplicates from list 
    Parameter:
        Sample List
    Return:
        Sorted List
    """
    updated_list = set(list)
    return updated_list
    

if __name__ == "__main__":
    sample_list = [1,2,3,4,5,6,2,3]
    result = function_duplicate_list(sample_list)
    logging.debug("List after removing duplicates value from {} is {}".format(sample_list, result))
