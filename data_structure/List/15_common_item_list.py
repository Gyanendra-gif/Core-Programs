"""
@Author: Gyanendra
@Date: 12/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 12/01/2021 
@Title : List in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_find_common_item(listOne, listTwo):
    """
    Description:
        Function is Used to find common items from two lists.
    Parameter:
        Sample Two List
    Return:
        True or False
    """
    result = []
    for i in listOne:
        if i in listTwo:
            result.append(i)
    return result
    
    
if __name__ == "__main__":
    sample_list_one = [1,2,3,4,5]
    sample_list_two = [6,7,8,9,1]
    result = function_find_common_item( sample_list_one, sample_list_two)
    logging.debug("Here are the common item in {} and {} are {}".format(sample_list_one, sample_list_two, result))
 