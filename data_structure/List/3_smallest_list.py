"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 11/01/2021 
@Title : List in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_smallest_list(list):
    """
    Description:
        Function is Used for finding smallest item from List 
    Parameter:
        Sample List
    Return:
        Minimum Value
    """
    value = list[0]
    for i in range(1,list.__len__()):
        if value > list[i]:
            value = list[i]
    return value

if __name__ == "__main__":
    sample_list = [20,31,43,12,58]
    result = function_smallest_list(sample_list)
    logging.debug("Smallest item in list {} is {}".format(sample_list, result))
