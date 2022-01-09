"""
@Author: Gyanendra
@Date: 09/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 09/01/2021 
@Title : Dictionary in Python
"""

def function_concat_dict(dic1, dic2, dic3):
    """
Description:
    Function is Used for Creating a Dictionary with taking key and value parameter from user
Parameter:
    Self to represent instance of class
Return:
    Created Dictionary
"""
    try:
        updated_dict = {}
        updated_dict.update(dic1)
        updated_dict.update(dic2)
        updated_dict.update(dic3)
    except TypeError:
        return updated_dict
    else:
        return updated_dict
    
if __name__ == "__main__":
    dic1 = {1:10, 2:20}
    dic2 = {3:30, 4:40}
    dic3 = {5:50, 6:60} 
    concated_dict = function_concat_dict(dic1,dic2,dic3)  
    print("Here is the Concated Dictionary: ", concated_dict)

