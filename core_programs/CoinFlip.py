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
      Taking Input From User as No. of Times Coin Should be Flip
Return:
      Percentage of Head and Tails i Flip
"""
import random
headCount = 0
tailCount = 1
count = int(input('How Many Time You Wants to Flip Coin'))
if count > 0:
    for x in range (count):
        flip = random.random()
        if flip < 0.5 :
             print('Head Occures')
             headCount = headCount + 1
        else:
             print('Tails Occures')
             tailCount = tailCount + 1
    headPercentage = int(headCount / count * 100)
    tailPercentage = 100 - headPercentage
    print('Head Percentage is: ' + str(headPercentage))
    print('Tail Percentage is: ' + str(tailPercentage))
else:
    print('Provide Correct Integer of Count')