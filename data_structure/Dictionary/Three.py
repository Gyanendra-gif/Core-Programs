"""
@Author: Gyanendra
@Date: 09/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 09/01/2021 
@Title : Dictionary in Python
"""

def square_dict(number):
    """
Description:
    Function is Used for Creating a Dictionary with taking number as parameter from user
Parameter:
    number from user to create square dictionary
Return:
    Created Dictionary
"""
    my_dict = {}
    for item in range(1,number+1):
        my_dict[item] = item*item
    return my_dict


if __name__ == '__main__':
    while True:
        try:
            user_input = int(input('Enter number in Integer Format: '))
        except ValueError:
            print('Error! Enter Proper Integer Only')
        else:
            break

    print(square_dict(user_input))