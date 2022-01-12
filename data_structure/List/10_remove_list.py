"""
@Author: Gyanendra
@Date: 12/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 12/01/2021 
@Title : List in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_removing_list(listOne):
    """
    Description:
        Function is takes specified list after removing the 0th, 4th and
        5th elements.
    Parameter:
        Sample List
    Return:
        Updated List
    """
    result = []
    specified = [0,4,5]
    for i in listOne:
        if listOne.index(i) not in specified:
            result.append(i)
    return result

if __name__ == "__main__":
    sample_list_one = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

    result = function_removing_list(sample_list_one)
    logging.debug("After removing 0, 4 and 5 item from {} is {}".format(sample_list_one, result))
