"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 10/01/2021 
@Title : Basic Programs in Python
"""

def function_histogram(list):
    """
Description:
    Function is Used for taking list as a parameter and print the symbol according to that 
Parameter:
    list
Return:
    Print the pattern according to list
"""
    for i in list:
        value = ' '
        times = i
        while(times > 0):
            value += '@'
            times = times - 1
        print(value)

if __name__ == "__main__":
    my_list = [2,4,7,10]
    function_histogram(my_list)     
          