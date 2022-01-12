"""
@Author: Gyanendra
@Date: 12/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 12/01/2021 
@Title : List in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_length_list(list, length):
    """
    Description:
        Function is Used for find the list of words that are longer than n from a
        given list of words.
    Parameter:
        Sample List
    Return:
        Updated List
    """
    result = []
    for i in list:
        if (i.__len__() > length):
            result.append(i)
    return result

if __name__ == "__main__":
    sample_list = ["Gyanendra", "Sam", "Harry", "Tom", "Can"]
    result = function_length_list(sample_list, 3)
    logging.debug("Items have more then three word {} is {}".format(sample_list, result))
