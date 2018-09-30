__author__= 'anjali'
import unittest
from selenium import webdriver

class login(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_login(self):
		user ="liken"
		pwd= "coolguyss"
		driver = webdriver.Firefox()
		driver.get("http://localhost:8000/login/?next=/")
		elem = driver.find_element_by_id("id_username")
		elem.send_keys(user)
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(pwd)
		driver.find_element_by_class_name('btn-block').click()
		driver.get("http://localhost:8000/settings/password/")
		old_password ="coolguyss"
		new_password= "coolguysss"
		new_password_confirmation= "coolguysss"
		elem = driver.find_element_by_id("id_old_password")
		elem.send_keys(old_password)
		elem = driver.find_element_by_id("id_new_password1")
		elem.send_keys(new_password)
		elem = driver.find_element_by_id("id_new_password2")
		elem.send_keys(new_password_confirmation)
		element =driver.find_element_by_id("change-password")
		print (element.text)
		element.click()
		
	def tearDown(self):
	        self.driver.quit()


		
		
if __name__ == '__main__':
	unittest.main()
