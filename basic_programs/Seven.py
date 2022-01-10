"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 10/01/2021 
@Title : Basic Programs in Python
"""

def function_find(value):
    """
Description:
    Function is Used for taking value from user and check it with the available data 
Parameter:
    value
Return:
    True or False based on Condition
"""
    test_data = [1,5,8,3]
    for i in test_data:
        if(i == value):
            return True
    return False        

if __name__ == "__main__":
    condition = True
    while (condition == True):
        try:
            user_input = int(input("Enter a Value to Check: "))
            result = function_find(user_input)  
            print(result)  
            userChoice = int(input('Press 0 to Continue the Program or 1 to stop the program: '))
            if (userChoice == 1):
                condition = False 
        except ValueError:
            print("Error! Enter Correct Integer")
        