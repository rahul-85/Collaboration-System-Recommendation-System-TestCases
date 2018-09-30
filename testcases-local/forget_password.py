__author__= 'anjali'
import unittest
from selenium import webdriver

class forget_password(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_forget_password(self):
		email= "anjaliagrawal41@gmail.com"
		driver = webdriver.Firefox()
		driver.get("http://localhost:8000/reset/")
		elem = driver.find_element_by_id("id_email")
		elem.send_keys(email)
		driver.find_element_by_id('reset').click()
		driver.find_element_by_xpath('//a[@href="/login/"]').click()
		
	def tearDown(self):
	        self.driver.quit()


if __name__ == '__main__':
	unittest.main()
