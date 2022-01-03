"""
@Author: Gyanendra
@Date: 01/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 01/01/2021 
@Title : Gyanendra
"""
class Contact:
    
    def __init__(self, first_name, last_name, address, city, state, zip, phone, email) -> None:
        """
Description:
    Function is Used for Initiating Object Properties (Getter, Setter) for AddressBook
Parameter:
      Object with their specific data type
Return:
       Updated Object as per our requirement
"""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.email = email

    def set_first_name (self, value):
        self.first_name = value

    def set_last_name (self, value):
        self.last_name = value
     
    def set_address (self, value):
        self.address = value 

    def set_city (self, value):
        self.city = value

    def set_state (self, value):
        self.state = value

    def set_zip (self, value):
        self.zip = value

    def set_phone (self, value):
        self.phone = value

    def set_email (self, value):
        self.email = value

    def get_first_name (self):
        return self.first_name

    def get_last_name (self):
        return self.first_name

    def get_last_name (self):
        return self.last_name

    def get_address (self):
        return self.address

    def get_city (self):
        return self.city    

    def get_state (self):
        return self.state

    def get_zip (self):
        return self.zip       

    def get_phone (self):
        return self.phone  

    def get_email (self):
        return self.email  
        