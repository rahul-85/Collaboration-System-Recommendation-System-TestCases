# Test cases for Recommendation System

## Prerequisites
1. The system should have some articles,users and community.
2. __Model must be trained before__.The system should have some recommendation showing in the recommendation list i.e., the model must be trained before execution of test_recommendation.py file. 
3. Please check that there should be some recommendation in the article. 

## Running Test Cases
This test case runs by executing the test_recommendation.py file

## Explaination
Login into Collaboration System .Open the Articles link, select an article. Open
the links in the recommendation list one by one and links should open without
any error.

## `.env` Variables
The requirements in the .env file:
1. __RECOMMENDATION_SYSTEM_DOCKER_ADDRESS__: This field is the ip address of the docker.
2. __RECOMMENDATION_SYSTEM_NAME__: This field is the username of any existing user in the system(prefered django admin).
3. __RECOMMENDATION_SYSTEM_PASSWORD__: This field is the password of above username.
4. __RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS__: This field is the ip address of the Collaborative system (with ports).
