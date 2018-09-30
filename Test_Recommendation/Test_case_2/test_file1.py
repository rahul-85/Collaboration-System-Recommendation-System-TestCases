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
	    #RECOMMENDATION_SYSTEM_DOCKER_ADDRESS = config("RECOMMENDATION_SYSTEM_DOCKER_ADDRESS")
	    #RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS=config("RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS")
	    self.driver = webdriver.Remote(command_executor='http://'+RECOMMENDATION_SYSTEM_DOCKER_ADDRESS+':4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)#,browser_profile=profile)
	    #RECOMMENDATION_SYSTEM_DJANGO_ADMIN_PASSWORD = config("RECOMMENDATION_SYSTEM_DJANGO_ADMIN_PASSWORD")
	    #RECOMMENDATION_SYSTEM_DJANGO_ADMIN_NAME = config("RECOMMENDATION_SYSTEM_DJANGO_ADMIN_NAME")
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

	    self.driver.maximize_window() #For maximizing window
	    self.driver.implicitly_wait(2000) #gives an implicit wait for 2 seconds
	    
	    self.log_in_django_admin()
	    for i in range(len(self.test_community)):
	    	self.create_community(self.test_community[i])
	    print('Communities created\n')
	    
	    for i in range(len(self.test_user)):
	    	self.create_user(self.test_user[i],self.master_password)
	    print('Users created\n')
	    self.log_out_django_admin()
	    
	    self.log_in(RECOMMENDATION_SYSTEM_DJANGO_ADMIN_NAME,RECOMMENDATION_SYSTEM_DJANGO_ADMIN_PASSWORD)
	    for i in range(len(self.test_community)):
	    	self.join_community(self.test_community[i])
	    print("Communities joined by "+RECOMMENDATION_SYSTEM_DJANGO_ADMIN_NAME)
	    self.log_in(RECOMMENDATION_SYSTEM_DJANGO_ADMIN_NAME,RECOMMENDATION_SYSTEM_DJANGO_ADMIN_PASSWORD)
	    for i in range(len(self.test_article_community_1)):
	    	self.create_article(self.test_community[0],self.test_article_community_1[i])
	    print('Community 1 Articles created\n')

	    for i in range(len(self.test_article_community_2)):
	    	self.create_article(self.test_community[1],self.test_article_community_2[i])
	    print('Community 2 Articles created\n')
	    self.log_out()

	    self.log_in(self.test_user[0],self.master_password)
	    self.join_community(self.test_community[0])
	    self.log_out()

	    self.log_in(self.test_user[1],self.master_password)
	    self.join_community(self.test_community[1])
	    self.log_out()

	    self.log_in_django_admin()
	    for i in range(len(self.test_article_community_1)):
	    	self.publish_article(self.test_article_community_1[i])
	    print('Community 1 Articles Published\n')

	    for i in range(len(self.test_article_community_2)):
	    	self.publish_article(self.test_article_community_2[i])
	    print('Community 2 Articles Published\n')
	    self.log_out_django_admin()	    

	def log_in_django_admin(self):
		print("Logging in to Django Admin")
		self.driver.get(self.django_admin_link)
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

	def create_community(self,name):
		print("Creating community "+name)
		self.driver.get(self.django_admin_link)
		self.driver.implicitly_wait(200)
		self.driver.find_element_by_link_text('Communitys').click()
		self.driver.implicitly_wait(200)
		self.driver.find_element_by_link_text('Add community').click()
		self.driver.implicitly_wait(200)
		self.driver.find_element_by_id("id_name").send_keys(name)
		self.driver.find_element_by_id("id_desc").send_keys('Testing Purpose')
		self.driver.find_element_by_id("id_category").send_keys(name)
		self.driver.find_element_by_id("id_tag_line").send_keys(name)
		self.driver.find_element_by_id("id_forum_link").send_keys(name)
		self.driver.find_element_by_id("id_image").send_keys(os.getcwd()+'/test.png')
		select = Select(self.driver.find_element_by_id("id_created_by"))
		select.select_by_visible_text(RECOMMENDATION_SYSTEM_DJANGO_ADMIN_NAME)
		self.driver.find_element_by_class_name('default').click()
		self.driver.implicitly_wait(200)
		print(name +" Community created successfully!\n")

	def create_user(self,name,pwd):
		print("Creating user "+name)
		self.driver.get(self.django_admin_link)
		self.driver.implicitly_wait(200)
		self.driver.find_element_by_link_text('Users').click()
		self.driver.implicitly_wait(200)
		self.driver.find_element_by_link_text('Add user').click()
		self.driver.implicitly_wait(200)
		self.driver.find_element_by_id("id_username").send_keys(name)
		self.driver.find_element_by_id("id_password1").send_keys(pwd)
		self.driver.find_element_by_id("id_password2").send_keys(pwd)
		self.driver.find_element_by_class_name('default').click()
		self.driver.implicitly_wait(200)
		self.driver.find_element_by_id("id_first_name").send_keys(name)
		self.driver.find_element_by_id("id_last_name").send_keys('tester')
		self.driver.find_element_by_id("id_email").send_keys('tester@gmail.com')
		self.driver.find_element_by_id("id_is_superuser").click()
		self.driver.find_element_by_id("id_groups_add_all_link").click()
		self.driver.find_element_by_id("id_user_permissions_add_all_link").click()
		self.driver.find_element_by_class_name('default').click()
		self.driver.implicitly_wait(200)
		print(name +" user created successfully!\n")

	def view_community(self,name):
		print("Viewing community "+name)
		self.driver.get(self.community_link)
		self.driver.implicitly_wait(800)
		elems=self.driver.find_elements_by_class_name('mix-details')
		elem=0
		for i in range(len(elems)):
			elems[i].click()
			if(elems[i].find_element_by_tag_name('h4').text==name):
				elem=elems[i]
				break
		elem.find_element_by_class_name('mix-link').click()
		self.driver.implicitly_wait(200)
		print("Viewed community "+name+"\n")

	def join_community(self,name):
		print("Joining to community "+name)
		self.view_community(name)
		self.driver.implicitly_wait(1000)
		self.driver.find_element_by_id('join-us').click()
		print("Joined to community "+name+"\n")

	def create_article(self,community_name,article_name):
		print("Creating an article "+article_name)
		self.view_community(community_name)
		self.driver.implicitly_wait(1000)
		self.driver.find_element_by_xpath("//button [@type='button' and @data-target='#modalCreate']").click()
		elem=self.driver.find_element_by_xpath("//button [@type='button' and @data-target='#modalCreateArticle']")
		actions = ActionChains(self.driver)
		#actions.move_to_element(elem).perform()
		# self.driver.execute_script("return arguments[0].scrollIntoView(true);", elem)
		self.driver.implicitly_wait(1000)
		elem.click()
		elem=self.driver.find_element_by_id("exampleCheck1")
		actions = ActionChains(self.driver)
		#actions.move_to_element(elem).perform()
		#self.driver.execute_script("return arguments[0].scrollIntoView(true);", elem)
		self.driver.implicitly_wait(1000)
		elem.click()
		self.driver.find_element_by_id("articleCreate").click()
		self.driver.implicitly_wait(1000)
		self.driver.find_element_by_id("title").send_keys(article_name)
		self.driver.find_element_by_id("create").click()
		self.driver.implicitly_wait(500)
		self.driver.get("http://" + RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS)
		print("Created an article "+article_name+"\n")

	def publish_article(self,name):
		print("Publishing article "+name)
		self.driver.get(self.django_admin_link)
		self.driver.implicitly_wait(500)
		self.driver.find_element_by_link_text('Articless').click()
		self.driver.implicitly_wait(500)
		self.driver.find_element_by_link_text(name).click()
		self.driver.implicitly_wait(500)
		self.driver.find_element_by_id("id_body").send_keys("Testing Purpose")
		self.driver.find_element_by_id("id_image").send_keys(os.getcwd()+'/test.png')
		select=Select(self.driver.find_element_by_id("id_state"))
		select.select_by_visible_text('publish')
		select=Select(self.driver.find_element_by_id("id_published_by"))
		select.select_by_visible_text(RECOMMENDATION_SYSTEM_DJANGO_ADMIN_NAME)
		self.driver.find_element_by_id("id_published_on_0").send_keys('12/02/2018')
		self.driver.find_element_by_id("id_published_on_1").send_keys('09:23:59')
		self.driver.find_element_by_class_name('default').click()
		self.driver.implicitly_wait(500)
		print("Published article "+name+"\n")

	def log_in(self,name,pwd):
		print("Logging in to Collaborative Communities")
		self.driver.get(self.login_link)
		self.driver.implicitly_wait(500)
		self.driver.find_element_by_id("id_username").send_keys(name)
		self.driver.find_element_by_id("id_password").send_keys(pwd)
		self.driver.find_element_by_class_name('btn-block').click()
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