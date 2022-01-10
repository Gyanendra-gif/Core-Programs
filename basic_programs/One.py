"""
@Author: Gyanendra
@Date: 09/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 09/01/2021 
@Title : Dictionary in Python
"""

def function_reverse_name():
    """
Description:
    Function is Used for taking first and last name from user and make it reverse
Parameter:
    first and last name 
Return:
    reversed name having space between them
"""

    first_name = input("Enter your First Name: ")
    last_name = input("Enter Your Last Name: ")
    print("Here is your Reversed Name: " + last_name + " " + first_name) 
    
if __name__ == "__main__":
    function_reverse_name()
       
