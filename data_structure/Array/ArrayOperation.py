"""
@Author: Gyanendra
@Date: 04/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 05/01/2021 
@Title : Array in Python
"""
from array import *

# Array Creation
number = array("i", [1,2,3,4,5])

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
    result = print(count)
    return result


# Remove First Occurence
def removeOccurence_array(number, element):
    count = 0
    for i in range(len(number)):
        if i == element:
            result = number.remove(element)
            break
    result = print(number)
    return result

if __name__ == "__main__":
    condition = True
    while (condition == True):

        choice = int(input("Enter the Option to Execute Array Operation Press"
                                                                            + "\n 1: To Print Array"
                                                                            + "\n 2: To Reverse Array" 
                                                                            + "\n 3: To Count Occurence of Element"
                                                                            + "\n 4: To Remove Occurence: "))
        if choice == 1:
            print_array(number)
        elif choice == 2:
            reverse_array(number)
        elif choice == 3:
            element = int(input("Enter The Element Whose Occurence is to be Check: "))
            occurence_array(number, element)
        elif choice == 4:
            element = int(input("Enter The Element Whose Occurence is to be Check: "))
            removeOccurence_array(number, element)
        else:
            print('Provide Correct Input in Range')
        userChoice = int(input('Press 0 to Continue the Program or 1 to stop the program: '))
        if (userChoice == 1):
            condition = False         

