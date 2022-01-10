"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 10/01/2021 
@Title : Dictionary in Python
"""

def function_nested_dict(list):
    """
Description:
    Function is Used for Creating Nested Dictionary
Parameter:
    List
Return:
    Updated Nested Dictionary
"""
    updated_dict = my_dict = {}
    for data in list:
        my_dict[data] = {}
        my_dict = my_dict[data]
    print("Here is Nested Dict: " ,updated_dict)

if __name__ == "__main__":
    sample_list = [1,2,3,4,5,6]
    function_nested_dict(sample_list)
