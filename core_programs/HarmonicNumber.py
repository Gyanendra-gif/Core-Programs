'''
@Author: Gyanendra
@Date: 2021-12-29
@Last Modified by: Gyanendra
@Last Modified time: 2021-12-29 
@Title : Take User Input And Find Nth Harmonic Sum
'''

"""
Description:
    Function description in depth
Parameter:
      Taking Input From User as Harmonic Value N  
Return:
     Sum of Nth Harmonic Number 
"""

number = int(input('Enter the Harmonic Value as Number: '))
while(number > 0):
    if number != 0:
        harmonic = 0
        for i in range (1, number + 1) :
            sum = harmonic + (1/i)
        print('Harmonic Number is: ', sum)
    else:
        print('Provide the Correct Number Should not Equal to 0')    