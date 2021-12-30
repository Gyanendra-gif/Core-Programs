'''
@Author: Gyanendra
@Date: 2021-12-29
@Last Modified by: Gyanendra
@Last Modified time: 2021-12-29 
@Title : Prime Factorization of a Number
'''

"""
Description:
    Function description in depth
Parameter:
      Taking Input From User and Calculate its Prime Factor
Return:
      Prime Factor of a Number
"""
number = int(input('Enter the Number to Check its Prime Factors:' ))
i = 2
while (i<=number):
    if (number%i==0):
        print(i, end=' ')
        number = number/i
    else:
        i += 1
