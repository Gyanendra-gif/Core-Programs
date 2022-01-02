'''
@Author: Gyanendra
@Date: 30/12/2021 
@Last Modified by: Gyanendra
@Last Modified time: 02/01/2021 
@Title : Gyanendra
'''

def function_wind(t,v):
     """
Description:
    Function description in depth
Parameter:
      Temprature and Speed of Wind
Return:
    It will return windchill
"""
     return (35.74 + 0.6215*t + (0.4275*t - 35.75)*pow(v,0.16))

try:
    t = int(input('Enter Temprature in Fahrenheit'))
    v = int(input('Enter Speed of wind in miles per hour'))  

    print('Here the wind chill is: ', function_wind(t, v))

except Exception as e:
    print(e)

