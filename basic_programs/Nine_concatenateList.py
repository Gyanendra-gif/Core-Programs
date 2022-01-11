"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 10/01/2021 
@Title : Basic Programs in Python
"""

def function_concate_elements(list):
    """
    Description:
        Function is Used for taking list as a parameter and print in a string format
    Parameter:
        list
    Return:
        Print the pattern according to list
    """
    data = " "
    for element in list:
        data += str(element)
    return data

if __name__ == "__main__":
    my_list = ['Welcome','to','Bridgelabz','Family']
    result = function_concate_elements(my_list)
    print(result)

