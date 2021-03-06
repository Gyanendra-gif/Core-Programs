"""
@Author: Gyanendra
@Date: 14/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 14/01/2021 
@Title : Tuple in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_create_tuple(lst):
    """
    Description:
        Function is Used for creating sample tuple with different data types
    Parameter:
        Sample List
    Return:
        Created tuple
    """
    sample_tuple = tuple(lst)
    return sample_tuple

if __name__ == "__main__":
    sample_list = [1,2,3,4,5,6,7.7,True, 'abc', 'xyz']
    result = function_create_tuple(sample_list)
    logging.debug("Here is the created tuple from list {} is {}".format(sample_list, result))
 
  