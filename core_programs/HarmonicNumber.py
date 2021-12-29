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
      Taking Input From User as Harmonic Value N  
Return:
      Nth Harmonic Number 
"""

from fractions import Fraction
number = int(input('Enter the Harmonic Value as number: '))
harmonic = 0
for i in range (1, number + 1) :
    harmonic = harmonic + (1/i)

print('Harmonic Number is: ' + str(Fraction(harmonic).limit_denominator(100)))