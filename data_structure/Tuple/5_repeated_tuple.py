"""
@Author: Gyanendra
@Date: 14/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 14/01/2021 
@Title : Tuple in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_repeated_tuple(tup):
    """
    Description:
        Function is Used to find the repeated items of a tuple.
    Parameter:
        Sample Tuple
    Return:
        Sample Set having repeated Number
    """
    new_tuple = set()
    for i in tup:
        if  tup.count(i) != 1:
            new_tuple.add(i)
    return new_tuple

if __name__ == "__main__":
    sample_tuple = (1,2,3,4,5,6,7,2,1)
    result = function_repeated_tuple(sample_tuple)
    logging.debug("Here is the repeated items from tuple {} is {}".format(sample_tuple, result))
  