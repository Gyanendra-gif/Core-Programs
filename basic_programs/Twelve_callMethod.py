"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 10/01/2021 
@Title : Basic Programs in Python
"""
import os

def function_callExternal_method():
    """
Description:
    Function is Used for taking path of the file and check it exist or not in the system 
Parameter:
    Path of the file
Return:
    None
"""
    print(os.system('ls -l'))

if __name__ == "__main__":
    function_callExternal_method()    
