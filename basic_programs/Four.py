"""
@Author: Gyanendra
@Date: 09/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 09/01/2021 
@Title : Basic Programs in Python
"""
import calendar

def function_calendar():
    """
Description:
    Function is Used for taking year and month from user and print calender 
Parameter:
    year and month 
Return:
    calendar of the given year and month
"""
    year = int(input("Enter the Year: "))
    month = int(input("Enter the Month: "))
    cal = print(calendar.month(year, month))
    return cal

if __name__ == "__main__":
    result = function_calendar()
    print('Here is the Calender of the given Month: ', result)