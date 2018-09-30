__author__= 'anjali'
import unittest
from selenium import webdriver

class article(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_article(self):
		driver = self.driver
		driver = webdriver.Firefox()
		driver.get("http://10.129.26.119//articles")
		driver.find_element_by_xpath("//a[@href='?page=2']").click()
		driver.find_element_by_xpath("//a[@href='?page=1']").click()
		driver.find_element_by_xpath("//a[@href='/article-view/14/']").click()
		driver.find_element_by_xpath("//a[@href='/article-view/14/']").click()
		message ="pancharkarm"
		name= "kl"
		mail= "anjali gtre"
		link= "gen"
		checkbox= "click"
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
		# driver.find_element_by_xpath("//a[@href='/https://en.wikipedia.org/wiki/Panchakarma/']").click()
		# driver.find_element_by_xpath("//a[@href='/https://en.wikipedia.org/wiki/Vamana/']").click()
		# driver.find_element_by_xpath("//a[@href='/https://en.wikipedia.org/wiki/Basti_(Panchakarma)/']").click()
		# driver.find_element_by_xpath("//a[@href='/https://en.wikipedia.org/wiki/Nasya/']").click()
		driver.find_element_by_xpath("//a[@href='/community-view/5/']").click()
		element =driver.find_element_by_class_name("btn-primary")
		driver.find_element_by_xpath("//a[@href='/forum/forum/ayurveda-6/']").click()

		
	def tearDown(self):
	    self.driver.quit()


if __name__ == '__main__':
	unittest.main()

		