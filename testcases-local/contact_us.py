__author__= 'anjali'
import unittest
from selenium import webdriver

class Login(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_Login(self):
		user ="liken"
		pwd= "coolguyss"
		driver = webdriver.Firefox()
		driver.get("http://localhost:8000/login/?next=/")
		elem = driver.find_element_by_id("id_username")
		elem.send_keys(user)
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(pwd)
		driver.find_element_by_class_name('btn-block').click()
		driver.get("http://localhost:8000/contact_us/")
		name="anj"
		email= "agrawal41@gmail.com"
		issue_type= "anjali gtre"
		message= "gen"
		elem = driver.find_element_by_id("contacts-name")
		elem.send_keys(name)
		elem = driver.find_element_by_id("contacts-email")
		elem.send_keys(email)
		elem = driver.find_element_by_id("issue")
		elem.send_keys(issue_type)
		elem = driver.find_element_by_id("contacts-message")
		elem.send_keys(message)
		driver.find_element_by_id('submit').click()
		driver.find_element_by_id('cancel').click()
	def tearDown(self):
	        self.driver.quit()


if __name__ == '__main__':
	unittest.main()

