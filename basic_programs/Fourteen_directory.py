"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 10/01/2021 
@Title : Basic Programs in Python
"""
import os
def function_directory_files(path):
    """
Description:
    Function is Used for taking path of the Directory and check for the files in the directory 
Parameter:
    Path of the directory
Return:
    None
"""
    try:
        file_list = os.listdir(path)
        print("Files and Directories are : ", file_list)
    except FileNotFoundError:
        print("Error! File not available")

if __name__ == "__main__":

    user_input = input("Enter Path of Directory: ")
    function_directory_files(user_input)