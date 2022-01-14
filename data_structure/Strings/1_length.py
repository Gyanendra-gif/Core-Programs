"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 11/01/2021 
@Title : Strings in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_length_string(str):
    """
    Description:
        Function is Used for creating sample tuple from the items of List 
    Parameter:
        Sample List
    Return:
        Created tuple
    """
    length = len(str) 
    return length

if __name__ == "__main__":
    sample_str = "Gyanendra"
    result = function_length_string(sample_str)
    logging.debug("Here is the length of the string {} is {} ".format(sample_str, result))
 
  