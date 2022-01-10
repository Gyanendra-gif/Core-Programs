"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 10/01/2021 
@Title : Basic Programs in Python
"""
import os

def function_enviroment():
    """
Description:
    Function is Used for taking list as a parameter and print the symbol according to that 
Parameter:
    list
Return:
    Print the pattern according to list
"""
    print("Here are the Enviroment Variables: ", os.environ)

if __name__ == "__main__":
    function_enviroment()    