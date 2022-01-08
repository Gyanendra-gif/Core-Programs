"""
@Author: Gyanendra
@Date: 02/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 03/01/2021 
@Title : Gyanendra
"""
from ContactAddress import Contacts

class AddressBook:
                           
        def add_contact(self):
                """
Description:
    Function is Used for taking Proper input from User with given parameters
Parameter:
      self parameter
Return:
       Object Create with given parameters
"""
                first_name = input('first name: ')
                last_name = input('lastName: ')
                address = input('address: ')
                city = input('city: ')
                state = input('state: ')
                zip = input('zip: ')
                phone = input('phone :')
                email = input('email: ')   

                return Contacts(first_name, last_name, address, city, state, zip, phone, email)

        def edit_contact(self, data):
                # contact = Contacts()

                choice = int(input('Enter Your Choice to Edit Contact, Press: '+'\n 1-First Name'+ '\n 2-Last Name'+'\n 3-Address'+'\n 4-City'
                                                + '\n 5-State'+'\n 6-Zip'+ '\n 7-Phone'+ '\n 8-Email' + '\n ->' ))
                while choice < 9 :
                        if(choice == 1):
                                data.first_name = input("Enter First Name: ")            
                                # contact.set_first_name(self.new_firstName)
                                break

                        elif(choice == 2):
                                data.last_name = input("Enter Last Name: ")
                                # contact.set_last_name(self.new_lastName)
                                break

                        elif(choice == 3):
                                data.address = input("Enter Address: ")
                                # contact.set_address(self.new_address)
                                break

                        elif(choice == 4):
                                data.city = input("Enter City: ")
                                # contact.set_city(self.new_city)
                                break

                        elif(choice == 5):
                                data.state = input("Enter State: ")
                                # contact.set_state(self.new_state)
                                break

                        elif(choice == 6):
                                data.zip = input("Enter Zip: ")
                                # contact.set_zip(self.new_zip)
                                break

                        elif(choice == 7):
                                data.phone = input("Enter Mobile Number: ")
                                # contact.set_phone(self.new_phone)
                                break

                        elif(choice == 8):
                                data.email = input("Enter Email: ")
                                # contact.set_email = self.new_email
                                break   

        def display_contact(self, contact_List):
                for contact in range(len(contact_List)):
                        print(vars(contact_List[contact]))  

                                       

        def delete_contact(self, contact_List):
                self.name = input("Enter the First Name of Contact you Want to Delete from AddressBook: ")
                for contact in contact_List:
                        print(contact[0].first_name)
                        if contact_List[0] == self.name:
                                del contact
                                print("Contact Deleted Successfully")  
                        else:
                                print("Enter Proper Correct Name")                     

if __name__ == "__main__":
        addressBook = AddressBook()
        contact_List = []
        condition = True
        while (condition == True):
            try:
                choice  = int(input('Enter Your Choice to Execute Program \n 1: Add Contact, \n 2: Edit Contact, \n 3: Display Contacts , \n 4: Delete Contacts, \n --'))
                if choice == 1:
                        addContact = addressBook.add_contact()
                        contact_List.append(addContact)
                elif choice == 2:
                        addressBook.edit_contact(contact_List[0])
                        addressBook.display_contact(contact_List)
                elif choice == 3:
                        addressBook.display_contact(contact_List)
                elif choice == 4:
                        addressBook.delete_contact(contact_List)
                else:
                        print('Enter Correct Option')
                userChoice = int(input('Press 0 to Continue the Program or 1 to stop the program: '))
                if (userChoice == 1):
                        condition = False    
            except ValueError:
                    print("Error!, Entered Value is not Integer")

                         
        

                        