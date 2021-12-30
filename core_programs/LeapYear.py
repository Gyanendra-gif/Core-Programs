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
year = input('Enter the Year to Check and it should be in four digit: ')
while (len(year) == 4):
    if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0 :
        print('Year in a Leap Year', int(year))
        break
    else: 
        print('Year is Not a Leap Year', int(year))
        break    