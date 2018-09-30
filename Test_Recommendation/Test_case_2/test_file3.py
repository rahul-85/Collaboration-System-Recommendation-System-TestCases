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



	def getTotalNumberOfPagesArticles(self):
		print("Getting total number of pages")
		self.driver.get(self.articles_link)
		self.driver.implicitly_wait(500)
		total=1
		elem=self.driver.find_element_by_class_name('col-md-4.col-sm-4.items-info')
		s=elem.text.split(' of ')
		s=s[-1].split('>')
		total=int(s[0])
		print("Got total number of pages "+str(total)+"\n")
		return total

	def view_article(self,name):
		print("Viewing an article "+name)
		flag=False
		elem1=None
		elem=[]
		total=1
		total=self.getTotalNumberOfPagesArticles()
		for i in range(1,total+1):
			self.driver.get(self.articles_link+'?page='+str(i))
			self.driver.implicitly_wait(1200)
			elem = self.driver.find_elements_by_tag_name('h3')
			for j in range(len(elem)):
				if(elem[j].text==name):
					elem1=elem[j]
					flag=True
					break
			if(flag==True):
				break
		elem1.find_element_by_link_text(name).click()
		self.driver.implicitly_wait(500)
		#self.driver.get("http://" + RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS)
		print("Viewed article "+name+"\n")

	def log_in(self,name,pwd):
		print("Logging in to Collaborative Communities")
		self.driver.get(self.login_link)
		self.driver.implicitly_wait(500)
		self.driver.find_element_by_id("id_username").send_keys(name)
		self.driver.find_element_by_id("id_password").send_keys(pwd)
		self.driver.find_element_by_class_name('btn-block').click()
		self.driver.implicitly_wait(500)
		print("Logged in to Collaborative Communities"+"\n")

	def log_out(self):
		print("Logging out from Collaborative Communities")
		self.driver.get(self.logout_link)
		self.driver.implicitly_wait(200)
		print("Logged out from Collaborative Communities"+"\n")

	def test_reco(self):
		self.log_in(self.test_user[-1],self.master_password)
		self.driver.implicitly_wait(200)
		self.view_article(self.test_article_community_1[-1])
		self.driver.implicitly_wait(200)
		print("Testing\n")
		elem=self.driver.find_elements_by_class_name('alert.alert-info')[1]
		elem1=elem.find_elements_by_tag_name('h5')
		if(len(elem1)!=0):
			number_of_community_article_1=0
			number_of_community_article_2=0
			number_of_other_community_article=0
			for i in range(len(elem1)):
				c=elem1[i].text
				if(c in self.test_article_community_1):
					number_of_community_article_1=number_of_community_article_1+1
				elif(c in self.test_article_community_2):
					number_of_community_article_2=number_of_community_article_2+1
				else:
					number_of_other_community_article=number_of_other_community_article+1
			print("Number of articles from test community 1 in the recommendation of test user 3: ",number_of_community_article_1)
			print("Number of articles from test community 2 in the recommendation of test user 3: ",number_of_community_article_2)
			print("Number of articles from other community(other than test community 1 and test community 2) in the recommendation of test user 3: ",number_of_other_community_article)
			# RECOMMENDATION_SYSTEM_MINIMUM_RECOMMENDATION_PERCENTAGE=int(config('MINIMUM_RECOMMENDATION_PERCENTAGE'))
			actual_reco_factor=number_of_community_article_1/len(elem1)*100
			if(actual_reco_factor>=RECOMMENDATION_SYSTEM_MINIMUM_RECOMMENDATION_PERCENTAGE):
				self.assertEqual(True,True)
			else:
				self.assertEqual(True,False)
		self.log_out()


	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()
