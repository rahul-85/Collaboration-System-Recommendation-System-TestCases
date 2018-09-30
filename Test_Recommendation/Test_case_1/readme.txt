This test case runs by executing the test_recommendation.py file.

The idea is that:

Login into Collaboration System .Open the Articles link, select an article. Open
the links in the recommendation list one by one and links should open without
any error.

###################################

The requirements in the .env file:

ADDRESS: This field is the ip address of the docker.
NAME: This field is the username of any existing user in the system(prefered django admin).
PASSWORD: This field is the password of above username.
DEPLOY_ADDRESS: This field is the ip address of the Collaborative system (with ports).

####################################

Note: The model must be trained after execution of test_recommendation.py file. Please check that there should be some recommendation in the article. 