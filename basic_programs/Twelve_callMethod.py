"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 11/01/2021 
@Title : Basic Programs in Python
"""
import os

def function_callExternal_method():
    """
    Description:
        Function is Used for calling outer method after importing os module 
    Parameter:
        None
    Return:
        None
    """
    print(os.system('cd ..'))

if __name__ == "__main__":
    function_callExternal_method()    
