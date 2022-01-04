"""
@Author: Gyanendra
@Date: 02/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 03/01/2021 
@Title : Gyanendra
"""
from ContactAddress import Contact

class AddressBook:                             

        def add_contact(self):
                first_name = input('first name: ')
                last_name = input('lastName: ')
                address = input('address: ')
                city = input('city: ')
                state = input('state: ')
                zip = input('zip: ')
                phone = input('phone :')
                email = input('email: ')   

                return Contact(first_name, last_name, address, city, state, zip, phone, email)
                

        def edit_contact(self):
                
                self.choice = int(input('Enter Your Choice to Edit Contact, Press: '+'\n 1-First Name'+ '\n 2-Last Name'+'\n 3-Address'+'\n 4-City'
                                                + '\n 5-State'+'\n 6-Zip'+ '\n 7-Phone'+ '\n 8-Email' + '\n ->' ))
                while self.choice < 9 :


                        if(self.choice == 1):
                                self.new_firstName = input("Enter First Name: ")            
                                Contact.set_first_name = self.new_firstName
                                break

                        elif(self.choice == 2):
                                self.new_lastName = input("Enter Last Name: ")
                                Contact.set_last_name = self.new_lastName
                                break

                        elif(self.choice == 3):
                                self.new_address = input("Enter Address: ")
                                Contact.set_address = self.new_address
                                break

                        elif(self.choice == 4):
                                self.new_city = input("Enter City: ")
                                Contact.set_city = self.new_city
                                break

                        elif(self.choice == 5):
                                self.new_state = input("Enter State: ")
                                Contact.set_state = self.new_state
                                break

                        elif(self.choice == 6):
                                self.new_zip = input("Enter Zip: ")
                                Contact.set_zip = self.new_zip
                                break

                        elif(self.choice == 7):
                                self.new_mobile = input("Enter Mobile Number: ")
                                Contact.set_phone = self.new_mobile
                                break

                        elif(self.choice == 8):
                                self.new_email = input("Enter Email: ")
                                Contact.set_email = self.new_email
                                break        
              
        def delete_contact(self, Contact):
                address = input('Enter the First Name you Want to Delete Contact')
                if address == Contact.get_first_name:
                         del Contact 
                else:
                        print('Provide Correct First Name')                         

        def display_contact(self):
                for i in ContactList:
                        print(i)                         

addressBook = AddressBook()
if __name__ == "__main__":
        ContactList = []

        choice  = int(input('Enter Your Choice to Execute Program \n 1: Add Contact, \n 2: Edit Contact, \n 3: Delete Contact , \n 4: Display Contacts, \n --'))
        if choice == 1:
               addContact = addressBook.add_contact()
               print(addContact)
        elif choice == 2:
                addressBook.edit_contact()
        elif choice == 3:
                addressBook.delete_contact(Contact)
        elif choice == 4:
                addressBook.display_contact()
        else:
                print('Enter Correct Option')                                        
                        