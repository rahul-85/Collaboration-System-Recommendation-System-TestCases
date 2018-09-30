__author__ = 'urmi'

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os

class NavbarActions(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		# self.driver.implicitly_wait(30)
		self.driver.maximize_window()
		# self.driver.get("http://10.129.26.119//login")
		# self.driver.find_element_by_id("id_username").send_keys("testuser")
		# self.driver.find_element_by_id("id_password").send_keys("collaborative")
		# self.driver.find_element_by_class_name('btn-block').click()

	# def test_navbar_about(self):
	# 	self.driver.find_element_by_xpath('//a[@href="/about_us/"]').click()

	def test_navbar_communities(self):
		self.driver.get("http://10.129.26.119")
		self.driver.find_element_by_xpath('//a[@href="/communities/"]').click()

	def test_navbar_articles(self):
		self.driver.get("http://10.129.26.119")
		self.driver.find_element_by_xpath('//a[@href="/articles/"]').click()

	def test_navbar_contact(self):
		self.driver.get("http://10.129.26.119")
		self.driver.find_element_by_xpath('//a[@href="/contact_us/"]').click()

	def test_navbar_faq(self):
		self.driver.get("http://10.129.26.119")
		self.driver.find_element_by_xpath('//a[@href="/FAQs/"]').click()
        
	def tearDown(self):
		# close the browser window
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()


    
