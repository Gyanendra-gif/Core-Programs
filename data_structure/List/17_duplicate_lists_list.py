"""
@Author: Gyanendra
@Date: 12/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 12/01/2021 
@Title : List in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_split_item(lst):
    """
    Description:
        Function is Used to remove duplicates from a list of lists.
    Parameter:
        Sample List
    Return:
        Updated List
    """
    my_list = []
    for i in lst:
        if my_list.count(i) == 0:
            my_list.append(i)
    return list(my_list)
    
    
if __name__ == "__main__":
    sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    result = function_split_item(sample_list)
    logging.debug("Here is the Updated list of {} after removing duplicates list is {}".format(sample_list, result))
 