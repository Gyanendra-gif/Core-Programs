"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 10/01/2021 
@Title : Dictionary in Python
"""

def function_multiple_keys(dict, string):

    """
Description:
    Function is Used for check multiple keys in dictionary
Parameter:
    Dictionary and String to Check Availibility of Keys in Dict.
Return:
    None
"""
    my_list = string.split()
    for i in my_list:
        if i in dict.keys():
            print("Available in Dictionary as key ", i)
        else:
            print("Not Available in Dictionary as key ", i)

if __name__ == "__main__":
    sample_dict = {"Sam": 1, "Tom": 2, "Can": 3}  
    sample_string = "Sam Harry"
    function_multiple_keys(sample_dict, sample_string)          