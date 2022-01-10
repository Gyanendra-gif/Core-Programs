"""
@Author: Gyanendra
@Date: 09/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 09/01/2021 
@Title : Dictionary in Python
"""
def unique_values(dict):
    """
Description:
    Function is Used for Finding Unique Data From Sample Dictionary
Parameter:
    Dictionary name to check unique values in it
Return:
    Unique Values from Dictionary
"""
    uniqueValues = set(dict.values())
    return uniqueValues

if __name__ == '__main__':
    sample_data = {"VA":"S001", "VB":"S002", "VI":"S001", "VC":"S005", "VII":"S005", "V":"S009", "VIII":"S007"}
    values = unique_values(sample_data)
    print("Here is the Unique Values from Dictionary: ", values)