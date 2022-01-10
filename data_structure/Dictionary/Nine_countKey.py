"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 10/01/2021 
@Title : Dictionary in Python
"""
def function_count(dict):
    count = 0
    for i in dict:
        if i['success'] == True:
            count = count + 1
    return count

if __name__ == "__main__":
    sample_dict = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
    False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
    result = function_count(sample_dict)
    print("Here is Count of Key Having Success: ", result)