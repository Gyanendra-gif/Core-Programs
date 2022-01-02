
'''
@Author: Gyanendra
@Date: 30/12/2021 
@Last Modified by: Gyanendra
@Last Modified time: 02/12/2021 
@Title : Gyanendra
'''
import math
def function_distance(x, y):
      """
Description:
    Function description in depth
Parameter:
      Two Co-ordinate X and Y
Return:
      Distance of the Co-ordinate from origin
"""
      return (math.pow((x*x + y*y), 0.5))

if __name__ == '__main__':

      x = int(input('Enter the X Co-ordinate: '))
      y = int(input('Enter the y Co-ordinate: '))
      print('The Distance of Co-ordinate from origin', function_distance(x, y))
else:
      print('Provide The Correct Integer Value')
