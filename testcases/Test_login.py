__author__ = 'urmi and minali'

import unittest
import LoginWrongCredentialsTest
import LoginCorrectCredentialsTest
import Test_navbar_actions
import os

class MyTestSuite(unittest.TestCase):

	def test_login_correct_credential(self):
		unittest.defaultTestLoader.loadTestsFromTestCase(LoginCorrectCredentialsTest.LoginCorrect)

	def test_login_wrong_credential(self):
		unittest.defaultTestLoader.loadTestsFromTestCase(LoginWrongCredentialsTest.LoginWrong)

	def test_navbar_actions(self):
		unittest.defaultTestLoader.loadTestsFromTestCase(Test_navbar_actions.NavbarActions)


if __name__ == '__main__':
	unittest.main()
