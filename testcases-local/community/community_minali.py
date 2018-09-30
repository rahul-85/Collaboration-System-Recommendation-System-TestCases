__author__= 'anjali'
import unittest
from selenium import webdriver

class Login(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_Login(self):
		user="liken"
		pwd= "coolguyss"
		driver = webdriver.Firefox()
		driver.maximize_window() #For maximizing window
		driver.implicitly_wait(20) #gives an implicit wait for 20 seconds
		driver.get("http://10.129.26.119//login")#
		elem = driver.find_element_by_id("id_username")
		elem.send_keys(user)
		elem = driver.find_element_by_id("id_password")
		elem.send_keys(pwd)
		driver.find_element_by_class_name('btn-block').click()
		driver.get("http://10.129.26.119//communities")
		driver.find_element_by_xpath('//a[@href="/community-view/42/"]').click()
		driver.find_element_by_xpath('//a[@href="/group-view/1/"]').click()
		driver.find_element_by_xpath('//a[@href="/community-view/42/"]').click()
		driver.find_element_by_xpath('//a[@href="/userprofile/Minali/"]').click()
		driver.find_element_by_xpath('//a[@href="/article-view/9/"]').click()
		driver.find_element_by_xpath('//a[@href="/comments/reply/4/"]').click()
		comment="gsfuasp;kfsb"
		checkbox="click"
		elem = driver.find_element_by_id("id_comment")
		elem.send_keys(comment)
		elem = driver.find_element_by_id("id_followup_4")
		elem.send_keys(checkbox)
		driver.find_element_by_class_name('btn-primary').click()
		driver.find_element_by_class_name('btn-default').click()
		message="bguisdfjmmns"
		checkbox="click"
		elem = driver.find_element_by_id("id_comment")
		elem.send_keys(message)
		elem = driver.find_element_by_id("id_followup")
		elem.send_keys(checkbox)
		driver.find_element_by_xpath('//a[@href="/community-view/42/"]').click()
		#print Firefox.current_url
		driver.find_element_by_xpath('//a[@href="/group-view/8/"]').click()
		#print Firefox.current_url
		driver.find_element_by_xpath('//a[@href="/community-view/42/"]').click()
		#driver.find_element_by_class_name('btn-info').click()
		#driver.find_element_by_xpath('//a[@href="?version_id1=41&version_id2=43"]').click()
		#driver.find_element_by_xpath('//a[@href="?version_id1=43&version_id2=44"]').click()
		#driver.find_elements_by_name('version_id2').click()

	def tearDown(self):
	        self.driver.quit()


if __name__ == '__main__':
	unittest.main()

		