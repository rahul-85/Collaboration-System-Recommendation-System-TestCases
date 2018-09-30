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
		driver.get("http://localhost:8000/create_faq/")
		category="publishable"
		order_no= "hab"
		question= "what is test?"
		answer= "gen"
		elem = driver.find_element_by_name("category")
		elem.send_keys(category)
		elem = driver.find_element_by_id("flow")
		elem.send_keys(order_no)
		elem = driver.find_element_by_id("question")
		elem.send_keys(question)
		elem = driver.find_element_by_name("answer")
		elem.send_keys(answer)
		element =driver.find_element_by_id("create")
		print (element.text)
		element.click()
		
		
	def tearDown(self):
	        self.driver.quit()


if __name__ == '__main__':
	unittest.main()

