"""
@Author: Gyanendra
@Date: 09/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 09/01/2021 
@Title : Basic Programs in Python
"""


def function_color():
    """
Description:
    Function is Used for taking color from a list and print first and last color from it
Parameter:
    none
Return:
    first and last color from color list
"""
    color_list = ["Red", "Green", "White", "Black"]
    print("First and Last Color from List is: ", "%s %s" % (color_list[0], color_list[-1]))

if __name__ == "__main__":
    function_color()