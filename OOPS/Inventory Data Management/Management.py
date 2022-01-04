"""
@Author: Gyanendra
@Date: 04/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 04/01/2021 
@Title : Gyanendra
"""
      
import os
def read_data():
    """
Description:
    Function Read Data From Json File
Parameter:
      None
Return:
     Read Data From Json File 
"""
    f = open("Core-Programs\OOPS\Inventory Data Management\Files\Demo.json", "r")
    print(f.read())
    f.close

def write_data():
    """
Description:
    Function Add Data in Json File
Parameter:
    Input Data From User
Return:
     Will Add Data into Json 
"""
    value = input("Enter the Data to Add into Json File: ")
    f = open("Core-Programs\OOPS\Inventory Data Management\Files\Demo.json", "a")
    f.write(value)
    f.close()

def overWrite_data():
    """
Description:
    Function Over Write Data in Json File
Parameter:
    Input Data From User
Return:
     Will Add Data into Json 
"""
    value = input("Enter More Data to Add into Json File: ")
    f = open("E:\Python Workspace\Core-Programs\OOPS\Inventory Data Management\demo.txt", "w")
    f.write(value)
    f.close()

def delete_data():
    """
Description:
    Function Will Delete Json File 
Parameter:
    Full Path of The File
Return:
     None
"""
    os.remove("Core-Programs\OOPS\Inventory Data Management\Files\Demo.json")

def create_data():
    """
Description:
    Function Will Create Empty Text File
Parameter:
    File Name
Return:
     Will Create Empty File
"""
    f = open("file.txt", "x")
    f.close

if __name__ == "__main__":
    choice = int(input("Enter Your Choice to Perform Operation Press: \n 1: To Read Data, \n 2: To Add Data, \n 3: To Over Write Data, \n 4: To Delete File, \n 5: To Create Empty File, \n ->"))
    if choice == 1:
        result = read_data()
        print("File got Read", result)
    elif choice == 2:
        result = write_data()
        print("Data Added Successfully ", result)
    elif choice == 3:
        result = delete_data()
        print("File Deleted Successfully ")
    elif choice == 4:
        result = create_data()
        print("File Created Successfully ")
    else:
        print("Provide Correct Option to Perform Operation")            