"""
@Author: Gyanendra
@Date: 14/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 14/01/2021 
@Title : Tuple in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_slice_tuple(tup):
    """
    Description:
        Function is Used for sliceing a tuple in a range of given index value
    Parameter:
        Sample Tuple
    Return:
        Updated Tuple 
    """
    slice_tuple = tup[2:5]
    return tuple(slice_tuple)

if __name__ == "__main__":
    sample_tuple = (1,2,3,6,5,2,3)
    result = function_slice_tuple(sample_tuple)
    logging.debug("The Slice tuple from the tuple {} is {}".format(sample_tuple, result))
