"""
@Author: Gyanendra
@Date: 12/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 12/01/2021 
@Title : List in Python
"""
import logging
import  copy
logging.basicConfig(level=logging.DEBUG)

def function_circularly_list(listOne, listTwo):
    """
    Description:
        Function is Used to check whether two lists are circularly identical.
    Parameter:
        Sample Two List
    Return:
        True or False
    """
    result=[]
    temp = listOne*2
    temp_index = 0

    if (len(listOne) != len(listTwo)):
        return False
    else:
        if (len(result) != len(listOne)):
            for i in listTwo:
                for j in range(temp_index, len(temp)):
                    if i == temp[j]:
                        result.append(j)
                        temp_index=j
                        break
        new_result = set(result)
        new_result = list(new_result)
        for i in range (len(listOne)-1):
            if new_result[i+1]-new_result[i] == 1:
                pass
            else:
                return False

        return True
    
    
if __name__ == "__main__":
    sample_list_one = [1,2,3]
    sample_list_two = [2,3,1]
    result = function_circularly_list( sample_list_one, sample_list_two)
    logging.debug("Here the list {} and {} are {} circularly identical".format(sample_list_one, sample_list_two, result))
 