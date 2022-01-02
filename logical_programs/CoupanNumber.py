'''
@Author: Gyanendra
@Date: 31/12/2021 
@Last Modified by: Gyanendra
@Last Modified time: 02/01/2021 
@Title : Gyanendra
'''
import random
result_list = []

def function_intInput(string):
    """
Description:
    Function is Used for Check Proper input from User
Parameter:
      String Should be Provided by User
Return:
       User Input
"""
    while True:
        try:
            return int(input(string))
        except ValueError:
            print('Enter valid Integer Input')
            continue

def function_couponGenerator(total_coupons):

    count = 0
    for i in range(total_coupons):
        while True:
            count += 1
            number = random.randint(10000,999999)
            if number not in result_list:
                result_list.append(number)
                break
    return count

try:    
    text = 'Enter the Coupan to be Generate: '
    total_coupons = function_intInput(text)
    randoms = function_couponGenerator(total_coupons)

    print('List of Total Random Number Need to have All Distinct Number ', result_list)
    print('Total Randoms Required: ', randoms)        

except Exception as e:
    print (e)     

