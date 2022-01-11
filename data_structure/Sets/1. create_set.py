"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 10/01/2021 
@Title : Dictionary in Python
"""
def function_create_set(list):
    """
Description:
    Function is Used for Creating Sample Set
Parameter:
    Sample List
Return:
    Created Set
"""
    sample_set = set(list)
    return sample_set

if __name__ == "__main__":
    sample_list = ["Tom", "Harry", "Sam"]
    result = function_create_set(sample_list)
    print("Here is the Sample of Created Set: ", result)    