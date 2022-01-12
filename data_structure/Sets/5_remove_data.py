"""
@Author: Gyanendra
@Date: 11/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 11/01/2021 
@Title : Set in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_remove_dataSet(set):
    """
    Description:
        Function is Used for Removing Items from set if that is available in it
    Parameter:
        Sample Set
    Return:
        Updated Set
    """
    user_input = input("Enter the Name to Remove from set ")
    list = user_input.split()
    for i in list:
        try:
            set.remove(i)
        except KeyError:
            print('Error! Data is not available is set')
            continue
    return set

sample_set = {'Sam', 'Tom', 'Harry'}
output = function_remove_dataSet(sample_set)
logging.debug("Here is the Updated Set is {} ".format(sample_set ,output))  