__author__= 'anjali'
import unittest
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException

class signup(unittest.TestCase):
	global alert

	def alert_accept():
  		try:
    			alert = fire.switch_to_alert()
    			print "Aler text:" + alert.text
    			alert.accept()
    			print "Alert detected, accept it"
    			return True
		except UnexpectedAlertPresentException:
    			print "Hum..., continue?"
    			return False
  		except NoAlertPresentException:
    			print "No alert here"
   		 	return False
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_signup(self):
		username ="like123"
		email= "anjaliagrawal41@gmail.com"
		password= "coolguys"
		password_confirmation= "coolguys"
		driver = webdriver.Firefox()
		driver.get("http://localhost:8000/signup/")
		elem = driver.find_element_by_id("username")
		elem.send_keys(username)
		elem = driver.find_element_by_id("email")
		elem.send_keys(email)
		elem = driver.find_element_by_id("password1")
		elem.send_keys(password)
		elem = driver.find_element_by_id("password2")
		elem.send_keys(password_confirmation)
		#elem = driver.find_element_by_id("id_Captcha")
		#elem.send_keys(Captcha)
		driver.find_element_by_id('submit').click()
		driver.get("http://localhost:8000/login/?next=/")

		
	def tearDown(self):
	        self.driver.quit()


if __name__ == '__main__':
	unittest.main()
