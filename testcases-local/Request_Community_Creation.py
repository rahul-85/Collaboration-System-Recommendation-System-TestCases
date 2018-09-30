__author__= 'anjali'
import unittest
from selenium import webdriver

class Login(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_Login(self):
		user ="liken"
		pwd= "coolguysss"
		driver = webdriver.Firefox()
		driver.get("http://localhost:8000/login/?next=/")
		elem = driver.find_element_by_id("id_username")
		elem.send_keys(user)
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(pwd)
		driver.find_element_by_class_name('btn-block').click()
		driver.get("http://localhost:8000/request_community_creation/")
		name ="hab"
		tag_line= "habli"
		description= "ghji"
		category= "abcdef"
		purpose= "all frg"
		elem = driver.find_element_by_id("name")
		elem.send_keys(name)
		elem = driver.find_element_by_id("tag_line")
		elem.send_keys(tag_line)
		elem = driver.find_element_by_name("desc")
		elem.send_keys(description)
		elem = driver.find_element_by_id("category")
		elem.send_keys(category)
		elem = driver.find_element_by_name("purpose")
		elem.send_keys(purpose)
		element =driver.find_element_by_id("submit")
		print (element.text)
		element.click()
		
	def tearDown(self):
		self.driver.quit()


		
		
if __name__ == '__main__':
	unittest.main()
