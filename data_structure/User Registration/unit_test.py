"""
@Author: Gyanendra
@Date: 16/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 16/01/2021 
@Title : Gyanendra
"""
import unittest
import module_user_registration as ur

class Validate(unittest.TestCase):

    def test_email(self):
        """
    Description:
        Function is Used for Testing the Email Address of User 
    Parameter:
        Sample String as Email
    Return:
        None
    """
        email = 'abc@gmail.com'
        actual = ur.function_email_validate(email)
        self.assertEqual(actual, True)

    def test_password(self):
        """
    Description:
        Function is Used for Testing the Password of User with having Eight Characters and one
        Upper case letter and having one numeric character also with one special char
    Parameter:
        Sample String
    Return:
        None
    """
        password = 'abc#1Bnw'
        actual = ur.function_password_validate(password)
        self.assertEqual(actual, True)

if __name__ == "__main__":
    unittest.main()


