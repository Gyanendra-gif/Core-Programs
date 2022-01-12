"""
@Author: Gyanendra
@Date: 12/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 12/01/2021 
@Title : List in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_copy_list(list):
    """
    Description:
        Function is Used for copy list to another list
    Parameter:
        Sample List
    Return:
        Updated List
    """
    updated_list = list.copy()
    return updated_list
    

if __name__ == "__main__":
    sample_list = [1,2,3,4,5,6,2,3]
    result = function_copy_list(sample_list)
    logging.debug("Cloned List of {} is {}".format(sample_list, result))
