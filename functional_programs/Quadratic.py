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
      Three Values as a,b and c
Return:
      Square Roots of a given Eq.
"""
print('Enter the values of the quadratic equation a*x*x + b*x + c')
a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))
c = int(input('Enter value of c: '))

delta = b*b - 4*a*c
rootOne = (-b + pow(delta,0.5))/(2*a)
rootTwo = (-b - pow(delta,0.5))/(2*a)
print(rootOne)
print(rootTwo)