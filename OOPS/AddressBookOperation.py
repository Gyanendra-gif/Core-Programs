"""
@Author: Gyanendra
@Date: 02/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 03/01/2021 
@Title : Gyanendra
"""
from ContactAddress import Contact

class AddressBook:

    try:           

        def add_contact():
            firstName = input('first name: ')
            lastName = input('lastName: ')
            address = input('address: ')
            city = input('city: ')
            state = input('state: ')
            zip = input('zip: ')
            mobile = input('phone :')
            email = input('email: ')   

            new_contact = Contact(firstName, lastName, address, city, state, zip, mobile, email)
            return new_contact

        def edit_contact(self, Contact):
            self.choice = int(input('Enter Your Choice to Edit Contact Press: '+'\n 1-First Name'+ '\n 2-Last Name'+'\n 3-Address'+'\n 4-City'
                                        + '\n 5-State'+'\n 6-Zip'+ '\n 7-Phone'+ '\n 8-Email'))
            while self.choice < 9 :

                if(self.choice == 1):
                    self.new_firstName = input("Enter First Name: ")            
                    Contact.set_first_name(self.new_firstName)

                elif(self.choice == 2):
                    self.new_lastName = input("Enter Last Name: ")
                    Contact.last_name = self.new_lastName

                elif(self.choice == 3):
                    self.new_address = input("Enter Address: ")
                    Contact.address = self.new_address

                elif(self.choice == 4):
                    self.new_city = input("Enter City: ")
                    Contact.city = self.new_city

                elif(self.choice == 5):
                    self.new_state = input("Enter State: ")
                    Contact.state = self.new_state

                elif(self.choice == 6):
                    self.new_zip = input("Enter Zip: ")
                    Contact.zip = self.new_zip

                elif(self.choice == 7):
                    self.new_mobile = input("Enter Mobile Number: ")
                    Contact.phone = self.new_mobile

                elif(self.choice == 8):
                    self.new_email = input("Enter Email: ")
                    Contact.email = self.new_email

                else:
                    print('Enter a Correct Number')

                return Contact
            
        def delete_contact(self, contact):
            address = input('Enter the First Name you Want to Delete Contact')
            if address == self.first_name:
                del contact  

    except Exception as e:
        print(e)





