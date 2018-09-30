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
	    self.min_recommendation=int(config('MINIMUM_RECOMMENDATION_PERCENTAGE'))
	    self.master_password='selenium123'
	    self.django_admin_link="http://" + RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS+ "/admin"
	    self.community_link="http://" + RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS+ "/communities/"
	    self.login_link="http://" + RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS+ "/login/?next=/"
	    self.articles_link="http://" + RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS+ "/articles"
	    self.logout_link="http://" + RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS+ "/logout/"
	    self.django_admin_link_logout="http://" + RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS+ "/admin/logout"
	    self.number_of_pages=-1
	    self.id_comm_article_1=[]
	    self.id_comm_article_2=[]
	    self.driver.maximize_window() #For maximizing window
	    self.driver.implicitly_wait(2000) #gives an implicit wait for 2 seconds

	    for i in range(len(self.test_article_community_1)):
	    	self.create_views(RECOMMENDATION_SYSTEM_DJANGO_ADMIN_NAME,RECOMMENDATION_SYSTEM_DJANGO_ADMIN_PASSWORD,self.test_article_community_1[i])

	    for i in range(len(self.test_article_community_2)):
	    	self.create_views(RECOMMENDATION_SYSTEM_DJANGO_ADMIN_NAME,RECOMMENDATION_SYSTEM_DJANGO_ADMIN_PASSWORD,self.test_article_community_2[i])	    

	    for i in range(len(self.test_user)):
	    	self.log_in(self.test_user[i],self.master_password)
	    	if(i==0):
	    		for j in range(len(self.number_of_views_1)):
	    			for k in range((self.number_of_views_1[j])):
	    				self.create_views(self.test_user[i],self.master_password,self.test_article_community_1[j])
	    	elif(i==1):
	    		for j in range(len(self.number_of_views_2)):
	    			for k in range((self.number_of_views_2[j])):
	    				self.create_views(self.test_user[i],self.master_password,self.test_article_community_2[j])
	    	else:
	    		for j in range(len(self.number_of_views_by_user_31)):
	    			for k in range((self.number_of_views_by_user_31[j])):
	    				self.create_views(self.test_user[i],self.master_password,self.test_article_community_1[j])
	    	self.log_out()
	    print("Done Set Up\n")

	def getTotalNumberOfPagesArticles(self):
		print("Getting total number of pages")
		if(self.number_of_pages==-1):
			self.driver.get(self.articles_link)
			self.driver.implicitly_wait(1000)
			total=1
			elem=self.driver.find_element_by_class_name('col-md-4.col-sm-4.items-info')
			s=elem.text.split(' of ')
			s=s[-1].split('>')
			total=int(s[0])
			print("Got total number of pages "+str(total)+"\n")
			self.number_of_pages=total
			return total
		else:
			return self.number_of_pages

	def view_article(self,name):
		if(name==self.test_article_community_1[0] and self.number_of_pages==-1):
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
			e=elem1.find_element_by_tag_name('a')
			s=e.get_attribute('href')
			article_id_1=int(s.split('/')[-2])
			self.id_comm_article_1=[article_id_1+i for i in range(6)]
			self.id_comm_article_2=[article_id_1+i for i in range(6,12)]
			e.click()
			self.driver.implicitly_wait(200)
			# self.driver.get("http://" + RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS)
			print("Viewed article "+name+"\n")
		else:
			self.view_article_by_id(name)

	def view_article_by_id(self,name):
		print("Viewing an article "+name+" by id")
		if(name in self.test_article_community_1):
			index_at=self.test_article_community_1.index(name)
			article_id=self.id_comm_article_1[index_at]
			article_link_by_id="http://" + RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS+ "/article-view/"+str(article_id)+"/"
			self.driver.get(article_link_by_id)
			self.driver.implicitly_wait(500)
		else:
			index_at=self.test_article_community_2.index(name)
			article_id=self.id_comm_article_2[index_at]
			article_link_by_id="http://" + RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS+ "/article-view/"+str(article_id)+"/"
			self.driver.get(article_link_by_id)
			self.driver.implicitly_wait(500)
		print("Viewed an article "+name+" by id")


	def create_views(self,by_user,pwd,to_article):
		self.log_out()
		self.log_in(by_user,pwd)
		self.view_article(to_article)
		self.log_out()
		self.log_in(by_user,pwd)
		print("Views Created successfully!\n")

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
		pass

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()