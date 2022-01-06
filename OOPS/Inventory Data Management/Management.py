"""
@Author: Gyanendra
@Date: 04/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 06/01/2021 
@Title : Gyanendra
"""
      
import os

def read_data(filePath):
    """
Description:
    Function is Used to Read the Data from the file with having these parameters
Parameter:
    File Path 
Return:
    Read Data From File 
"""
    f = open(filePath, "r")
    print(f.read())
    f.close 
    
def write_data(filePath):
    """
Description:
    Function is Used to Add the Data from the file with having these parameters
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
    Function is Used to Write the Data from the file with having these parameters
Parameter:
    Input Data From User
Return:
    Will Add Data into File 
"""
    value = input("Enter More Data to Add into File: ")
    f = open(filePath, "w")
    result = f.write(value)
    f.close()
    return result

def delete_data(filePath):
    """
Description:
    Function is Used to Delete the file with having these parameters
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
    try:
        f = open(fileName, "x")
        f.close
    except Exception as e:
        print(e)    
      
if __name__ == "__main__":
    condition = False
    while (condition == False):
        try:
            
            choice = int(input("Enter Your Choice to Perform Operation Press:"
                                                        + "\n 1: To Read Data"
                                                        + "\n 2: To Write Data" 
                                                        + "\n 3: To Over Write Data"
                                                        + "\n 4: To Delete File"
                                                        + "\n 5: To Create File: "))
        
            if (choice == 1):
                filePath = input("Enter the Path of The File to Read Data: ")
                read_data(filePath)
            elif (choice == 2):
                filePath = input("Enter the Path of The File to Write Data: ")
                write_data(filePath)
            elif (choice == 3):
                filePath = input("Enter the Path of The File to Add More Data: ")
                overWrite_data(filePath)
            elif (choice == 4):
                filePath = input("Enter the Path of The File to Remove File: ")
                os.remove(filePath)
            elif (choice == 5):
                fileName = input("Enter the Name of File with Extension to Create Empty File: ")
            else:
                print("Enter the Opt. in range to execute the program")     
                    
            userChoice = int(input("Press 0 to Continue Program and 1 to Close Program: "))
            if (userChoice == 1):
                condition = True
            break                

        except ValueError:
            print("Error! Enter the correct integer to excute program")            





    