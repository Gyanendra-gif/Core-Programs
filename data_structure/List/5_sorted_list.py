"""
@Author: Gyanendra
@Date: 12/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 12/01/2021 
@Title : List in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_sorted_list(list):
    """
    Description:
        Function is Used for sorted list in increasing order by the last
        element in each tuple from a given list of non-empty tuples.
    Parameter:
        Sample List
    Return:
        Sorted List
    """
    temp = []
    temp.append(list[0])
    for i in range(1,5):
        for item in range(temp.__len__()):
            if temp[item][1] > list[i][1]:
                temp.insert(item, list[i])
                break
    return temp

if __name__ == "__main__":
    sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    result = function_sorted_list(sample_list)
    logging.debug("Items in Increasing Order of List {} is {}".format(sample_list, result))
