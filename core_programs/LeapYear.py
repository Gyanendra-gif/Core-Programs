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
      Taking Input From User as a Year to Check 
Return:
      Leap Year or Non Leap Year
"""
year = int(input('Enter the Year to Check and it should be in four digit'))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    print('Year in a Leap Year')
else: 
    print('Year is Not a Leap Year')    