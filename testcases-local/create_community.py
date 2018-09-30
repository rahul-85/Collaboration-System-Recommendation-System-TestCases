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
		driver.maximize_window() #For maximizing window
		driver.implicitly_wait(20) #gives an implicit wait for 20 seconds
		driver.get("http://localhost:8000/login/?next=/")
		elem = driver.find_element_by_id("id_username")
		elem.send_keys(user)
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(pwd)
		driver.find_element_by_class_name('btn-block').click()
		driver.get("http://localhost:8000/create_community/")
		name ="anj"
		tag_line= "kl"
		description= "anjali gtre"
		category= "gen"
		username= "like"
		community_Image="index.jpeg"
		elem = driver.find_element_by_id("name")
		elem.send_keys(name)
		elem = driver.find_element_by_id("tag_line")
		elem.send_keys(tag_line)
		elem = driver.find_element_by_name("desc")
		elem.send_keys(description)
		elem = driver.find_element_by_id("category")
		elem.send_keys(category)
		elem = driver.find_element_by_id("username")
		elem.send_keys(username)
		element = driver.find_element_by_id("community_image")
		element.send_keys("/home/frg/Pictures/images/index.jpeg")
		element =driver.find_element_by_id("create")
		print (element.text)
		element.click()
		
	
	def tearDown(self):
	        self.driver.quit()


if __name__ == '__main__':
	unittest.main()
