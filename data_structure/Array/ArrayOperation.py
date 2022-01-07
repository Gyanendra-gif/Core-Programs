"""
@Author: Gyanendra
@Date: 04/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 06/01/2021 
@Title : Array in Python
"""
from array import *

# Array Creation
# number = array("i", [])
def create_array():
    number = array("i", [])
    element = int(input("Enter The Number of Elements to Add is Array: "))
    for i in range (0, element):
        index = int(input("Enter Number at Index: "))
        number.append(index)
        print("Created Array is: ", number) 
        return number       

# Print Array
def print_array(number):
    for i in range(len(number)):
        print(number[i])

# Reverse Array
def reverse_array(number):  
    for i in reversed(number):
        print(i)
  
# Occurence of Element
def occurence_array(number, element):
    count = 0
    for i in range(len(number)):
        if i == element:
            count = count + 1
            break
    print(count)

# Remove First Occurence
def removeOccurence_array(number, element):
    count = 0
    for i in range(len(number)):
        if i == element:
            number.remove(element)
            break
    print(number)   

if __name__ == "__main__":
    
    """
Description:
    Function is Used for Operate the Array Operation after taking input from user
    and it will return the respective output
"""
    
    condition = True
    while (condition == True):
        try:
            choice = int(input("Enter the Option to Execute Array Operation Press"
                                                                            + "\n 1: To Create Array"
                                                                            + "\n 2: To Print Array"
                                                                            + "\n 3: To Reverse Array" 
                                                                            + "\n 4: To Count Occurence of Element"
                                                                            + "\n 5: To Remove Occurence: "))
        
            if choice == 1:
                value = create_array()
            elif choice == 2:
                print_array(value)
            elif choice == 3:
                reverse_array(value)
            elif choice == 4:
                element = int(input("Enter The Element Whose Occurence is to be Check: "))
                occurence_array(value, element)
            elif choice == 5:
                element = int(input("Enter The Element Whose Occurence is to be Remove: "))
                removeOccurence_array(value, element)
            else:
                print('Provide Correct Input in Range')
            userChoice = int(input('Press 0 to Continue the Program or 1 to stop the program: '))
            if (userChoice == 1):
                condition = False    
        except ValueError:
            print("Error!, Entered Value is not Integer")             

