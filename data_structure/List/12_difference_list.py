"""
@Author: Gyanendra
@Date: 12/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 12/01/2021 
@Title : List in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_difference_list(listOne, listTwo):
    """
    Description:
        Function is Used for calculating difference between two list
    Parameter:
        Sample List
    Return:
        Sorted List
    """
    result = list(set(listOne) - set(listTwo)) + list(set(listTwo) - set(listOne))
    return result
    
if __name__ == "__main__":
    sample_list_one = [1,2,3]
    sample_list_two = [3,4,5]
    result = function_difference_list( sample_list_one, sample_list_two)
    logging.debug("Difference from {} to {} is {}".format(sample_list_one, sample_list_two, result))
 