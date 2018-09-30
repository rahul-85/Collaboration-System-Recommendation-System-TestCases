import os
import unittest
from selenium import webdriver
from decouple import config
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

RECOMMENDATION_SYSTEM_DOCKER_ADDRESS = config("RECOMMENDATION_SYSTEM_DOCKER_ADDRESS")
RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS=config("RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS")
RECOMMENDATION_SYSTEM_DJANGO_ADMIN_PASSWORD = config("RECOMMENDATION_SYSTEM_DJANGO_ADMIN_PASSWORD")
RECOMMENDATION_SYSTEM_DJANGO_ADMIN_NAME = config("RECOMMENDATION_SYSTEM_DJANGO_ADMIN_NAME")
RECOMMENDATION_SYSTEM_MINIMUM_RECOMMENDATION_PERCENTAGE=int(config('RECOMMENDATION_SYSTEM_MINIMUM_RECOMMENDATION_PERCENTAGE'))


class TestRecommendation(unittest.TestCase):
	def setUp(self):
	    profile = webdriver.FirefoxProfile()
	    profile.set_preference("network.proxy.type", 1)
	    profile.set_preference("network.proxy.http","proxy.cse.iitb.ac.in")
	    profile.set_preference("network.proxy.http_port", 80)
	    profile.update_preferences()
	    profile.default_preferences['network.proxy.type']=0
	    #self.driver = webdriver.Firefox(profile)
	    # RECOMMENDATION_SYSTEM_DOCKER_ADDRESS = config("ADDRESS")
	    # RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS=config("DEPLOY_ADDRESS")
	    self.driver = webdriver.Remote(command_executor='http://'+RECOMMENDATION_SYSTEM_DOCKER_ADDRESS+':4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)#,browser_profile=profile)
	    # RECOMMENDATION_SYSTEM_DJANGO_ADMIN_PASSWORD = config("DJANGO_ADMIN_PASSWORD")
	    # RECOMMENDATION_SYSTEM_DJANGO_ADMIN_NAME = config("DJANGO_ADMIN_NAME")
	    # print(RECOMMENDATION_SYSTEM_DJANGO_ADMIN_NAME)
	    # print(RECOMMENDATION_SYSTEM_DJANGO_ADMIN_PASSWORD)
	    # print(RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS)

	    self.test_community=['test_community_'+str(i) for i in range(1,3)]
	    self.test_user=['test_user_'+str(i) for i in range(1,4)]
	    self.test_article_community_1=["test_article_community_1"+str(i) for i in range(1,7)]
	    self.test_article_community_2=["test_article_community_2"+str(i) for i in range(1,7)]
	    self.number_of_views_1=[9,7,1,0,0,0]  # by test_user_1 in test_community_1 articles'
	    self.number_of_views_2=[9,7,1,0,0,0]  # by test_user_2 in test_community_2 articles'
	    self.number_of_views_by_user_31=[0,1,2,1,0,0] # number of views by user 3 to test_community_1 articles'
	    # After above views by test_user_3 checking recommendation in test_user_3 for all articles

	    # RECOMMENDATION_SYSTEM_MINIMUM_RECOMMENDATION_PERCENTAGE=int(config('MINIMUM_RECOMMENDATION_PERCENTAGE'))
	    self.master_password='selenium123'
	    self.django_admin_link="http://" + RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS+ "/admin"
	    self.community_link="http://" + RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS+ "/communities/"
	    self.login_link="http://" + RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS+ "/login/?next=/"
	    self.articles_link="http://" + RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS+ "/articles"
	    self.logout_link="http://" + RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS+ "/logout/"
	    self.django_admin_link_logout="http://" + RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS+ "/admin/logout"
	    self.driver.maximize_window() #For maximizing window
	    self.driver.implicitly_wait(2000) #gives an implicit wait for 2 seconds

	def log_in_django_admin(self):
		print("Logging in to Django Admin")
		self.driver.get(self.django_admin_link)
		self.driver.implicitly_wait(500)
		self.driver.find_element_by_id("id_username").send_keys(RECOMMENDATION_SYSTEM_DJANGO_ADMIN_NAME)
		self.driver.find_element_by_id("id_password").send_keys(RECOMMENDATION_SYSTEM_DJANGO_ADMIN_PASSWORD)
		self.driver.find_element_by_class_name('submit-row').click()
		self.driver.implicitly_wait(200)
		print("Logged in to Django Admin\n")

	def log_out_django_admin(self):
		print("Logging out from Django Admin")
		self.driver.get(self.django_admin_link_logout)
		self.driver.implicitly_wait(200)
		print("Logged out from Django Admin\n")

	def remove_community(self,name):
		print("Removing community "+name)
		self.driver.get(self.django_admin_link)
		self.driver.implicitly_wait(200)
		self.driver.find_element_by_link_text('Communitys').click()
		self.driver.implicitly_wait(200)
		self.driver.find_element_by_link_text(name).click()
		self.driver.implicitly_wait(200)
		self.driver.find_element_by_class_name('deletelink').click()
		self.driver.implicitly_wait(200)
		self.driver.find_elements_by_tag_name("input")[2].click()
		self.driver.implicitly_wait(200)
		print(name+" Community removed successfully!\n")

	def remove_user(self,name):
		print("Removing user "+name)
		self.driver.get(self.django_admin_link)
		self.driver.implicitly_wait(200)
		self.driver.find_element_by_link_text('Users').click()
		self.driver.implicitly_wait(200)
		self.driver.find_element_by_id('searchbar').send_keys(name)
		elems=self.driver.find_elements_by_tag_name('input')
		elems[1].click()
		self.driver.implicitly_wait(200)
		self.driver.find_element_by_link_text(name).click()
		self.driver.implicitly_wait(200)
		self.driver.find_element_by_class_name('deletelink').click()
		self.driver.implicitly_wait(500)
		self.driver.find_elements_by_tag_name("input")[2].click()
		self.driver.implicitly_wait(200)
		print(name+" user removed successfully!\n")

	def remove_article(self,name):
		print("Removing article "+name)
		self.driver.get(self.django_admin_link)
		self.driver.find_element_by_link_text('Articless').click()
		self.driver.implicitly_wait(200)
		self.driver.find_element_by_link_text(name).click()
		self.driver.implicitly_wait(200)
		self.driver.find_element_by_class_name('deletelink').click()
		self.driver.implicitly_wait(200)
		self.driver.find_elements_by_tag_name("input")[2].click()
		self.driver.implicitly_wait(200)
		print("Removed article "+name+" successfully!"+"\n")

	def test_reco(self):
		pass

	def tearDown(self):
		self.log_in_django_admin()
		for i in range(len(self.test_article_community_1)):
			self.remove_article(self.test_article_community_1[i])
		print('Community 1 Articles removed\n')

		for i in range(len(self.test_article_community_2)):
			self.remove_article(self.test_article_community_2[i])
		print('Community 2 Articles removed\n')

		for i in range(len(self.test_user)):
			self.remove_user(self.test_user[i])
		print('Users removed\n')

		for i in range(len(self.test_community)):
			self.remove_community(self.test_community[i])
		print('Communities removed\n')
		self.log_out_django_admin()
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()