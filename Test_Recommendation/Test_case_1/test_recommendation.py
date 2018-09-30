import unittest
from selenium import webdriver
from decouple import config
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

RECOMMENDATION_SYSTEM_DOCKER_ADDRESS = config("RECOMMENDATION_SYSTEM_DOCKER_ADDRESS")
RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS=config("RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS")
RECOMMENDATION_SYSTEM_PASSWORD = config("RECOMMENDATION_SYSTEM_PASSWORD")
RECOMMENDATION_SYSTEM_NAME = config("RECOMMENDATION_SYSTEM_NAME")

class TestRecommendation(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox()
	    # RECOMMENDATION_SYSTEM_DOCKER_ADDRESS = config("RECOMMENDATION_SYSTEM_ADDRESS")
        self.driver = webdriver.Remote(command_executor='http://'+RECOMMENDATION_SYSTEM_DOCKER_ADDRESS+':4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)
        # RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS=config("RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS")
        # RECOMMENDATION_SYSTEM_PASSWORD = config("RECOMMENDATION_SYSTEM_PASSWORD")
        # RECOMMENDATION_SYSTEM_NAME = config("RECOMMENDATION_SYSTEM_NAME")
        #print(RECOMMENDATION_SYSTEM_NAME)
        #print(RECOMMENDATION_SYSTEM_PASSWORD)
        #print(RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS)
        self.login_link="http://" + RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS+ "/login/?next=/"
        self.article_link="http://"+RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS +"/articles/"
        #print(self.article_link)
        #print(self.login_link)
        self.logout_link="http://"+ RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS+ "/logout/"
        #print(self.logout_link)
        self.driver.maximize_window() #For maximizing window
        self.driver.implicitly_wait(20) #gives an implicit wait for 20 seconds
        self.driver.get(self.login_link)
        elem = self.driver.find_element_by_id("id_username")
        elem.send_keys(RECOMMENDATION_SYSTEM_NAME)
        elem = self.driver.find_element_by_id("id_password")
        elem.send_keys(RECOMMENDATION_SYSTEM_PASSWORD)
        self.driver.find_element_by_class_name('btn-block').click()

    def test_recommendation(self):
        self.driver.get(self.article_link)
        self.driver.implicitly_wait(2000)
        elem = self.driver.find_elements_by_tag_name('h3')
        name=elem[0].text
        self.driver.find_element_by_link_text(name).click()
        self.driver.implicitly_wait(2000)
        elem=self.driver.find_elements_by_class_name('alert.alert-info')[1]
        elem1=elem.find_elements_by_tag_name('h5')
        n=len(elem1)
        for i in range(n):
            self.driver.implicitly_wait(20)
            elem1=elem.find_elements_by_tag_name('h5')
            c=elem1[i].text
            #print(c)
            self.driver.find_element_by_link_text(c).click()
            self.driver.implicitly_wait(2000)
            assert "Page not found" not in self.driver.page_source
            self.driver.get(self.article_link)
            self.driver.implicitly_wait(2000)
            elem = self.driver.find_elements_by_tag_name('h3')
            name=elem[0].text
            self.driver.find_element_by_link_text(name).click()
            self.driver.implicitly_wait(2000)
            elem=self.driver.find_elements_by_class_name('alert.alert-info')[1]
            elem1=elem.find_elements_by_tag_name('h5')

    def tearDown(self):
        self.driver.get(self.logout_link)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
