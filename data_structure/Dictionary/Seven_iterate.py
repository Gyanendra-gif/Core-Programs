"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 10/01/2021 
@Title : Basic Programs in Python
"""
def sort_by_values(dict):
    """
    Description:
        Function is Used for Counting Letters From Sample String
    Parameter:
        String to Count its Letters
    Return:
        Dictionary with having letters in it
    """
    for key in dict:
        print(key, 'Corresponds to', dict[key])

if __name__ == "__main__":

    my_dict = {1:'Tom', 2:'Sam'}
    sort_by_values(my_dict)
    