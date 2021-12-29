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
      Taking Input From User Having Minimum Three Characters
Return:
      Hello Name , How Are You
"""

isCorrect = True
while isCorrect == True :
    name = input('Provide Your Name: ' )
    if  len(name) >= 3 : 
        print ('Hello' + name + ', How Are You')
        isCorrect = False
    else :
        print ('Please Provide Correct Name having 3 Characters Only')
