"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 10/01/2021 
@Title : Dictionary in Python
"""

def function_table_dict(dict):
    """
Description:
    Function is Used for Printing Data in table format
Parameter:
    Sample Dictionary
Return:
    None
"""
    for data in dict:
        print(data, '\t', dict[data])

if __name__ == "__main__":
    sample_dict = {'1':'Gyanendra', '2':'Sam', '3':'Tom', '4':'Cat'}
    function_table_dict(sample_dict)