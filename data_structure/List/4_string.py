"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 12/01/2021 
@Title : List in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_string_list(list):
    """
    Description:
        Function is Used for count the number of strings where the string length
        is 2 or more and the first and last character are same from a given list of strings.
    Parameter:
        Sample List
    Return:
        Count
    """
    count = 0
    for char in list:
        if len(char) > 1 and char[0] == char[-1]:
            count += 1
    return count

if __name__ == "__main__":
    sample_list = ['abc', 'xyz', 'aba', '1221']
    result = function_string_list(sample_list)
    logging.debug("Number of item count in list {} is {}".format(sample_list, result))
