"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 11/01/2021 
@Title : List in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_add_list(list):
    """
    Description:
        Function is Used for Adding the items of List 
    Parameter:
        Sample List
    Return:
        Created Set
    """
    count = 0
    for item in list:
        count = count + item
    return count

sample_list = [1,2,3,4,5,6,7]
result = function_add_list(sample_list)
logging.debug("Sum of all items in list {} is {}".format(sample_list, result))
 
  