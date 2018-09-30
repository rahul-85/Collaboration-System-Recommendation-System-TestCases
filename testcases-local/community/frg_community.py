__author__= 'anjali'
import unittest
from selenium import webdriver
import re


class Login(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_Login(self):
		user="liken"
		pwd= "coolguyss"
		#community_id_pattern = r.compile('/community-view/[0-9]+')
		driver = webdriver.Firefox()
		driver.maximize_window() #For maximizing window
		driver.implicitly_wait(20) #gives an implicit wait for 20 seconds
		driver.get("http://10.129.26.119//login")
		elem = driver.find_element_by_id("id_username")
		elem.send_keys(user)
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(pwd)
		driver.find_element_by_class_name('btn-block').click()
		driver.get("http://10.129.26.119//communities")
		driver.find_element_by_xpath('//a[@href="/community-view/42/"]').click()
		driver.find_element_by_xpath('//a[@href="/group-view/1/"]').click()
		driver.find_element_by_xpath('//a[@href="/community-view/42/"]').click()
		# print ("driver.current_url>>>>>>"+driver.current_url)
		

	def tearDown(self):
	    self.driver.quit()


if __name__ == '__main__':
	unittest.main()

		