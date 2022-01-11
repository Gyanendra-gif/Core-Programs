"""
@Author: Gyanendra
@Date: 09/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 09/01/2021 
@Title : Dictionary in Python
"""

def string_to_dict(string):
    """
    Description:
        Function is Used for Counting Letters From Sample String
    Parameter:
        String to Count its Letters
    Return:
        Dictionary with having letters in it
    """
    my_list = list(string)
    set_my_list = set(my_list)
    my_dict = {}
    for i in set_my_list:
        my_dict[i] = my_list.count(i)
    return my_dict


if __name__ == '__main__':
    sample_string =  'w3resource'
    result = string_to_dict(sample_string)
    print("Here is the Count of Letters: ", result)