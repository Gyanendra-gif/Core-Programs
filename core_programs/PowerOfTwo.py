'''
@Author: Gyanendra
@Date: 2021-12-29
@Last Modified by: Gyanendra
@Last Modified time: 2021-12-29 
@Title : Take User Input and Replace it with String
'''

"""
Description:
    Function description in depth
Parameter:
      Taking Input From User as N  
Return:
      Power of Two 
"""
exponent = int(input('Enter N to Check Power of Two'))
list = []
for i in range (1, exponent+1) :
    list.append(int(i**2))

print(list)
