"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 10/01/2021 
@Title : Basic Programs in Python
"""

def function_file(path):
    """
Description:
    Function is Used for taking path of the file and check it exist or not in the system 
Parameter:
    Path of the file
Return:
    None
"""
    try:
        my_file = open(path)
        print("File Available")
        my_file.close
    except FileNotFoundError:
        print("Error! File not available")

if __name__ == "__main__":

    user_input = input("Enter Path of File")
    function_file(user_input)

