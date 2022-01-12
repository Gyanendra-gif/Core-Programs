"""
@Author: Gyanendra
@Date: 12/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 12/01/2021 
@Title : List in Python
"""
import logging
import  copy
logging.basicConfig(level=logging.DEBUG)

def function_append_list(listOne, listTwo):
    """
    Description:
        Function is Used for append one list to another
    Parameter:
        Sample List
    Return:
        Sorted List
    """
    result = copy.copy(listOne)
    for i in listTwo:
        result.append(i)
    return result
    
    
if __name__ == "__main__":
    sample_list_one = [1,2,3]
    sample_list_two = [3,4,5]
    result = function_append_list( sample_list_one, sample_list_two)
    logging.debug("Copy from {} to {} is {}".format(sample_list_one, sample_list_two, result))
 