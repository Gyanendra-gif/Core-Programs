
'''
@Author: Author Name
@Date: 30/12/2021 
@Last Modified by: Gyanendra
@Last Modified time: 30/12/2021 
@Title : Gyanendra
'''
"""
Description:
    Function description in depth
Parameter:
      Two Co-ordinate X and Y
Return:
      Distance of the Co-ordinate from origin
"""
import math
x = int(input('Enter the X Co-ordinate: '))
y = int(input('Enter the y Co-ordinate: '))
distance = math.pow((x*x + y*y), 0.5)
print('The Distance of x,y from origin is: ', distance)
