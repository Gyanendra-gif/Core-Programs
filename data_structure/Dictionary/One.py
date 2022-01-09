"""
@Author: Gyanendra
@Date: 09/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 09/01/2021 
@Title : Dictionary in Python
"""

class Dictionary:

    # Create Dictionary
    def function_create_dict(self):
        """
Description:
    Function is Used for Creating a Dictionary with taking key and value parameter from user
Parameter:
    Self to represent instance of class
Return:
    Created Dictionary
"""
        my_dict = {}
        key = input("Enter Key for My Dictionary: ")
        value = input("Enter Value for My Dictionary: ")
        my_dict[key] = value
        print('My New Dictionary is: ', my_dict)
        return my_dict

    # Add Data to My Dictionary
    def function_add_to_dict(self, dict_name):
        """
Description:
    Function is Used for Adding Data in Dictionary
Parameter:
    Dictionary name to add key and values in it
Return:
    Updated Dictionary
"""
        key = input("Enter Key: ")
        value = input("Enter Value: ")
        dict_name[key] = value
        print('Updated Dictionary is: ', dict_name)
        return dict_name             
        

if __name__ == "__main__":
    dict = Dictionary()
    """
Description:
    Function is Used for Operate the Dictionary Operation after taking input from user
    and it will return the respective output
"""
    
    condition = True
    while (condition == True):
        try:
            choice = int(input("Enter the Option to Execute Dictionary Operation Press"
                                                                            + "\n 1: To Create Dictionary"
                                                                            + "\n 2: To Add Data to My Dictionary: " ))    
            if choice == 1:
                value = dict.function_create_dict()
                print("Dictionary Created Successfully: ")
            elif choice == 2:
                dict.function_add_to_dict(value)
            else:
                print('Enter Correct Output in Range')           
            userChoice = int(input('Press 0 to Continue the Program or 1 to stop the program: '))
            if (userChoice == 1):
                    condition = False    
        except ValueError:
            print("Error!, Entered Value is not Integer")      
            