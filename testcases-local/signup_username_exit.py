__author__= 'anjali'
import unittest
from selenium import webdriver
#
class signup(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_signup(self):
		username ="liken"
		email= "anjaliagrawal41@gmail.com"
		password= "coolguyss"
		password_confirmation= "coolguyss"
		driver = webdriver.Firefox()
		driver.get("http://localhost:8000/signup/")
		elem = driver.find_element_by_id("username")
		elem.send_keys(username)
		elem = driver.find_element_by_id("email")
		elem.send_keys(email)
		elem = driver.find_element_by_id("password1")
		elem.send_keys(password)
		elem = driver.find_element_by_id("password2")
		elem.send_keys(password_confirmation)
		#elem = driver.find_element_by_id("id_Captcha")
		#elem.send_keys(Captcha)
		driver.find_element_by_id('submit').click()
		driver.get("http://localhost:8000/login/?next=/")

		
	def tearDown(self):
	        self.driver.quit()


if __name__ == '__main__':
	unittest.main()
