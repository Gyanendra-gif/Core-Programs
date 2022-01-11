"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 10/01/2021 
@Title : Dictionary in Python
"""

def function_list_as_dictValue(dict):
    """
Description:
    Function is Used for check List Values available in dictionary
Parameter:
    Dictionary whose value is to be checked
Return:
    Count of List available in Dictionary
"""
    count = 0
    my_list = []
    for i in dict:
        if type(dict[i]) == type(my_list):
            count = count + 1
    return count

if __name__ == "__main__":
    sample_dict = {"Sam": [1,2,3,4,5], "Tom": 23, "Can": 48, "Harry": [23, 45,63]}
    result = function_list_as_dictValue(sample_dict)
    print("Here is the Count of Items in Dictionary Value that is List: ", result)   
