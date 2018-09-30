__author__= 'anjali'
import unittest
from selenium import webdriver

class loginincorrect(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_loginincorrect(self):
		user ="like"
		pwd= "cool12345"
		driver = webdriver.Firefox()
		driver.get("http://localhost:8000/login/?next=/")
		elem = driver.find_element_by_id("id_username")
		elem.send_keys(user)
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(pwd)
		driver.find_element_by_class_name('btn-block').click()
	def tearDown(self):
	        self.driver.quit()


		
		
if __name__ == '__main__':
	unittest.main()
