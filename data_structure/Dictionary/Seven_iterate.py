"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 10/01/2021 
@Title : Basic Programs in Python
"""
def sort_by_values(dict):
    for key in dict:
        print(key, 'Corresponds to', dict[key])

if __name__ == "__main___":
    my_dict = {'Tom': 1, 'Sam': 2, 'Ram': 3}
    sort_by_values(my_dict)
    