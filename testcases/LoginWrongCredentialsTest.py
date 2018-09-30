__author__ = 'urmi and minali'

import unittest
from selenium import webdriver

class LoginWrong(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_LoginWrong(self):
		user ="testuser"
		pwd= "collaborative123"
		driver = webdriver.Firefox()
		driver.get("http://10.129.26.119/login")
		elem = driver.find_element_by_id("id_username")
		elem.send_keys(user)
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(pwd)
		driver.find_element_by_class_name('btn-block').click()
		driver.find_element_by_class_name("alert-danger").text

if __name__ == '__main__':
	unittest.main()
