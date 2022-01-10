"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 10/01/2021 
@Title : Basic Programs in Python
"""
import multiprocessing

def function_cpu_count():
    """
Description:
    Function is Used for Calculating count of cpu
Parameter:
    Path of the file
Return:
    None
"""
    print(multiprocessing.cpu_count())

if __name__ == "__main__":
    function_cpu_count()