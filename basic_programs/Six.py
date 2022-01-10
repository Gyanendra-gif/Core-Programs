"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 10/01/2021 
@Title : Basic Programs in Python
"""

from datetime import date

def function_calculate_days():
    """
Description:
    Function is Used for Calculating number of days between two given dates
Parameter:
    None 
Return:
    Will give out the number of days between given dates
"""
    first_date = date(2014, 7, 2)
    last_date = date(2014, 7, 11)
    result = (last_date - first_date)
    print("Here is the number of days between first day and last day is: ", result.days)

if __name__ == "__main__":
    function_calculate_days()
