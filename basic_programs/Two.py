"""
@Author: Gyanendra
@Date: 09/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 09/01/2021 
@Title : Basic Programs in Python
"""

def function_list_tuple():
    """
Description:
    Function is Used for taking Comma Seprated Values from user and make it list and tuple
Parameter:
    None
Return:
    list and tuple after taking values from user 
"""
    values = input("Enter Some Comma Seprated Numbers: ")
    my_list = values.split(",")
    my_tuple = tuple(my_list)
    print("The List is: ", my_list)
    print("The Tuple is: ", my_tuple)

if __name__ == "__main__":
    function_list_tuple()    