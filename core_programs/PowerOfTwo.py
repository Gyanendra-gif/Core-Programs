'''
@Author: Gyanendra
@Date: 2021-12-29
@Last Modified by: Gyanendra
@Last Modified time: 2021-12-29 
@Title : Take User Input and Provide Power of two
'''

"""
Description:
    Function description in depth
Parameter:
      Taking Input From User as N  
Return:
      Power of Two 
"""
exponent = int(input('Enter N to Check Power of Two '))
if (0<=exponent<31):
    for i in range (1, exponent+1):
        print('2 ^',i,'=', pow(2, i))

else:
    print('Please Provide Exponent in Range Of 0 to 31')