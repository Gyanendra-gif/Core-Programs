"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 12/01/2021 
@Title : List in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_smallest_list(list):
    """
    Description:
        Function is Used for count the number of strings where the string length
        is 2 or more and the first and last character are same from a given list of strings.
    Parameter:
        Sample List
    Return:
        Count
    """
    temp = []
    for i in list:
        if (len(i) >+ 2):
            temp.append(i[0] + i[-1])
    for item in temp:
        if temp.count(item) != 1:
            return temp.count(item)
        else:
            return 'Nothing Available as per Requirement'

if __name__ == "__main__":
    sample_list = ['abc', 'xyz', 'azc', '1221']
    result = function_smallest_list(sample_list)
    logging.debug("Number of item count in list {} is {}".format(sample_list, result))
