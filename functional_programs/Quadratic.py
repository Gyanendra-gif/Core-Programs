'''
@Author: Author Name
@Date: 30/12/2021 
@Last Modified by: Gyanendra
@Last Modified time: 02/01/2021 
@Title : Gyanendra
'''
import math

def function_roots(a,b,c):
      """
Description:
    Function description in depth
Parameter:
      Three Values as a,b and c
Return:
      Square Roots of a given Eq.
"""
      delta = b*b - 4*a*c
      roots_list = []
      rootOne =(-b + pow(delta,0.5))/(2*a)
      roots_list.append(rootOne)

      rootTwo = (-b - pow(delta,0.5))/(2*a)
      roots_list.append(rootTwo)

      return roots_list
try:         
      print('Enter the values of the quadratic equation a*x*x + b*x + c')
      a = int(input('Enter value of a: '))
      b = int(input('Enter value of b: '))
      c = int(input('Enter value of c: '))

      print('Roots of Given Equation are: ', function_roots(a,b,c))

except Exception as e:
    print(e)