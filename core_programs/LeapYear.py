'''
@Author: Gyanendra
@Date: 2021-12-29
@Last Modified by: Gyanendra
@Last Modified time: 2021-12-29 
@Title : Take User Input Year and Check for Its Leap Year or Not
'''

"""
Description:
    Function description in depth
Parameter:
      Taking Input From User as a Year to Check 
Return:
      Leap Year or Non Leap Year
"""
year = int(input('Enter the Year to Check and it should be in four digit: '))
while (year > 999 and year < 10000):
    if(year) % 4 == 0 and(year) % 100 != 0 or(year) % 400 == 0 :
        print('Year in a Leap Year',(year))
        break
    else: 
        print('Year is Not a Leap Year',(year))
        break    