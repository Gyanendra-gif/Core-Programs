"""
@Author: Gyanendra
@Date: 11/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 11/01/2021 
@Title : Dictionary in Python
"""
def function_iterate_set(set):
    """
Description:
    Function is Used for Iterating Set
Parameter:
    Sample Set
Return:
    None
"""
    for value in set:
        print(value, end=" ")

if __name__ == "__main__":
    sample_set = {1,2,3,4,5,6,7,8,9,10}
    function_iterate_set(sample_set)
      