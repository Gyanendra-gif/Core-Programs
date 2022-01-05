"""
@Author: Gyanendra
@Date: 04/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 05/01/2021 
@Title : Gyanendra
"""
      
import os

def read_data(filePath):
    """
Description:
    Function Read Data From File
Parameter:
      File Path 
Return:
     Read Data From File 
"""
    f = open(filePath, "r")
    result = print(f.read())
    f.close
    # return result
    
def write_data(filePath):
    """
Description:
    Function Add Data in  File
Parameter:
    Input Data From User
Return:
     Will Add Data into File
"""
    value = input("Enter the Data to Add into File: ")
    f = open(filePath, "a")
    result = f.write(value)
    f.close()
    return result

def overWrite_data(filePath):
    """
Description:
    Function Over Write Data in  File
Parameter:
    Input Data From User
Return:
     Will Add Data into Json 
"""
    value = input("Enter More Data to Add into File: ")
    f = open(filePath, "w")
    result = f.write(value)
    f.close()
    return result

def delete_data(filePath):
    """
Description:
    Function Will Delete  File 
Parameter:
    Full Path of The File
Return:
     None
"""
    os.remove(filePath)

def create_file(fileName):
    """
Description:
    Function Will Create Empty Text File
Parameter:
    File Name
Return:
     Will Create Empty File
"""
    f = open(fileName, "x")
    f.close

def operation(choice):
    filePath = input("Enter the Path of The File: ")
    switcher = {
        1: read_data(filePath),
        2: write_data(filePath),
        3: overWrite_data(filePath),
        4: delete_data(filePath),       
    }
    switcher.get(choice, "Option Not Available")
      
if __name__ == "__main__":
    condition = True
    while (condition == True):
        choice = int(input("Enter Your Choice to Perform Operation Press:"
                                                        + "\n 1: To Read Data"
                                                        + "\n 2: To Write Data" 
                                                        + "\n 3: To Over Write Data"
                                                        + "\n 4: To Delete File: "))
        operation(choice)
        userChoice = int(input("Press 0 to Continue Program and 1 to Close Program"))
        if (userChoice == 1):
            condition = False





    