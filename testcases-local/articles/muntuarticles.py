__author__= 'anjali'
import unittest
from selenium import webdriver

class article(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_article(self):
		message ="classical"
		name= "kl"
		mail= "anjali gtre"
		link= "gen"
		checkbox= "click"
		driver = webdriver.Firefox()
		driver.get("http://10.129.26.119//articles")
		driver.find_element_by_xpath('//a[@href="/article-view/16/"]').click()
		driver.find_element_by_xpath('//a[@href="/articles/?page=1"]').click()
		driver.find_element_by_xpath('//a[@href="/articles/?page=2"]').click()
		elem = driver.find_element_by_id("id_comment")
		elem.send_keys(message)
		elem = driver.find_element_by_id("id_name")
		elem.send_keys(name)
		elem = driver.find_element_by_id("id_email")
		elem.send_keys(mail)
		elem = driver.find_element_by_id("id_url")
		elem.send_keys(link)
		elem = driver.find_element_by_id("id_followup")
		elem.send_keys(checkbox)
		element =driver.find_element_by_class_name("btn-primary")
		element =driver.find_element_by_class_name("btn-default")
		print (element.text)
		element.click()
		driver.find_element_by_xpath("//a[@href='/article-view/16/']").click()
		driver.find_element_by_xpath("//a[@href='/community-view/17/']").click()
		driver.find_element_by_xpath("//a[@href='/article-view/16/']").click()
		element =driver.find_element_by_class_name("btn-primary")
		driver.find_element_by_xpath('//a[@href="/forum/forum/forts-and-palaces-18/"]').click()
		
		
	def tearDown(self):
	    self.driver.quit()


if __name__ == '__main__':
	unittest.main()

		