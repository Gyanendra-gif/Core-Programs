"""
@Author: Gyanendra
@Date: 09/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 09/01/2021 
@Title : Dictionary in Python
"""

def function_add_to_dict():
        """
Description:
    Function is Used for Adding Data in Dictionary
Parameter:
    Dictionary name to add key and values in it
Return:
    Updated Dictionary
"""
        my_dict = {}
        key = input("Enter Key: ")
        value = input("Enter Value: ")
        my_dict[key] = value
        print('Created Dictionary is: ', my_dict)
        return my_dict 

def function_removeKey_from_dict(dict_name):
    """
Description:
    Function is Used for Removing Key Data from Dictionary
Parameter:
    Name of Dictionary
Return:
    Dictionary after key Remove
"""
    while True:
        try:
            while True:
                try:
                    user_input = str(input('Enter Key to Remove: '))
                except ValueError:
                    print('Error! Enter Numbers Only')
                    continue
                else:
                    break    
            dict_name.pop(user_input)
        except KeyError:
            print('Error! Enter key is invalid')
            continue
        else:
            break
    return dict_name

if __name__ == "__main__":
    """
Description:
    Function is Used for Operate the Dictionary Operation after taking input from user
    and it will return the respective output
"""
    
    condition = True
    while (condition == True):
        try:
            choice = int(input("Enter the Option to Execute Dictionary Operation Press"
                                                                            + "\n 1: To Add Keys and Value in Dictionary"
                                                                            + "\n 2: To Remove Keys from Dictionary: " ))    
            if choice == 1:
                value = function_add_to_dict()
                print("Dictionary Created Successfully: ")
            elif choice == 2:
                function_removeKey_from_dict(value)
                print("Key Removed Successfully")
            else:
                print('Enter Correct Output in Range')           
            userChoice = int(input('Press 0 to Continue the Program or 1 to stop the program: '))
            if (userChoice == 1):
                    condition = False    
        except ValueError:
            print("Error!, Entered Value is not Integer")                         

    
    
            

    

    
