"""
@Author: Gyanendra
@Date: 09/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 09/01/2021 
@Title : Basic Programs in Python
"""
def function_abs(number):
    """
Description:
    Function is Used for taking int as number and provide correct value
Parameter:
    Number as int from user 
Return:
    calendar of the given year and month
"""
    print("Absolute Value of Number is: ", abs(number))

if __name__ == "__main__":
    try:
        user_input = int(input('Enter Number to find ablsolute value: '))
        function_abs(user_input)    

    except TypeError:
        print('Error! Provide Correct Integer Type')