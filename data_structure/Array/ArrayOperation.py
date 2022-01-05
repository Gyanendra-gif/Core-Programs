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
    for i in range(len(number)):
        print(number.reverse())

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
    choice = int(input('Enter the Option to Execute Array Operation Press: \n 1: To Print Array, \n 2: To Reverse Array, \n 3: To Count Occurence of Element, \n 4: To Remove Occurence, \n -> '))
    if choice == 1:
        print_array(number)
    elif choice == 2:
        reverse_array(number)
    elif choice == 3:
        occurence_array(number, 3)
    elif choice == 4:
        removeOccurence_array(number, 2)
    else:
        print('Provide Correct Input in Range')        







            

