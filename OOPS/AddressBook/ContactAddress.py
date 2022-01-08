"""
@Author: Gyanendra
@Date: 01/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 01/01/2021 
@Title : Gyanendra
"""
class Contacts:
    def __init__(self, first_name, last_name, address, city, state, zip, phone, email) -> None:
        """
    Description:
        Function is Used for Initiate the Object with the given parameters
    Parameter:
        self object with having strings and int parameters
    Return:
        Object Create with given parameters
        """    
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.email = email

