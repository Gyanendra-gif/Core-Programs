"""
@Author: Gyanendra
@Date: 12/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 12/01/2021 
@Title : List in Python
"""
import logging
logging.basicConfig(level=logging.DEBUG)

def function_split_item(list):
    """
    Description:
        Function is Used to split a list based on first character of word.
    Parameter:
        Sample Two List
    Return:
        True or False
    """
    my_dict = {}
    for i in list:
        if i[0] not in my_dict.keys():
            my_dict[i[0]] = [i]
        else:
            my_dict[i[0]].append(i)
    return my_dict
    
    
if __name__ == "__main__":
    sample_list = ["Sam", "Tom", "Harry", "Michal"]
    result = function_split_item(sample_list)
    logging.debug("Here is the Dictionary based on first character of list item {} is {}".format(sample_list, result))
 