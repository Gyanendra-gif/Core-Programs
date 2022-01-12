"""
@Author: Gyanendra
@Date: 12/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 12/01/2021 
@Title : List in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_common_list(listOne, listTwo):
    """
    Description:
        Function is takes two lists and returns True if they have at
        least one common member.
    Parameter:
        Sample List
    Return:
        Updated List
    """
    for i in listOne:
        if i in listTwo:
            return True
    return False

if __name__ == "__main__":
    sample_list_one = [1,2,3,4,5,6]
    sample_list_two = [11,12,13,14,15,16,5]

    result = function_common_list(sample_list_one, sample_list_two)
    logging.debug("First List {} and {} when compared get {} ".format(sample_list_one, sample_list_two, result))
