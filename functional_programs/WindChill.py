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
      Temprature and Speed of Wind
Return:
    It will return windchill
"""
 
t = int(input('Enter Temprature in Fahrenheit'))
v = int(input('Enter Speed of wind in miles per hour'))

if(t<50 and 3<v<150):
    w = 35.74 + 0.6215*t + (0.4275*t - 35.75)*pow(v,0.16)
    print('Here the wind chill is: ', w)
else:
    print('Enter Correct Details as per specification')

