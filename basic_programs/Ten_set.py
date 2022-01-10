"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 10/01/2021 
@Title : Basic Programs in Python
"""

def function_set_color():
    """
Description:
    Function is Used for taking list as a parameter and print the symbol according to that 
Parameter:
    list
Return:
    Print the pattern according to list
"""
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    color_list_3 = (color_list_1.difference(color_list_2))
    print("Here is the Color which is not present in list two: ", color_list_3)

if __name__ == "__main__":
    function_set_color()    