__author__ = 'urmi and minali'

import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class LoginCorrect(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Remote(command_executor='http://10.129.132.104:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX) 
        #self.driver = webdriver.Firefox()
        

    def test_LoginCorrect(self):
        user ="testuser"
        pwd= "collaborative"
        driver = webdriver.Remote(command_executor='http://10.129.132.104:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX) 

        #driver = webdriver.Firefox()
        driver.get("http://10.129.26.119//login")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        driver.find_element_by_class_name('btn-block').click()


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
