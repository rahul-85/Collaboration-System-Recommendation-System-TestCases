# Test Case 2

## Overview
1. This test case runs by executing the test_file_driver.py file which runs all other python script.
2. No need to run other python file other than the test_file_driver.py.
3. The test_file1.py and test_file2.py set up the environment for this test case.
4. The test_file3.py contains the test_reco function which test the recommendation.
5. The test_file4.py tear down (remove) the environment which is required to run this test case.

__IMPORTANT__. test_file1.py create 2 communities, 3 users, 6 articles in each communities by django-admin.
test_file2.py give views to the articles of test_community_1 using test_user_1 and same for test_community_2 by test_user_3.
And test_user_3 gives some views(lesser than) to articles of test_community_1. For more information see idea given below.

## Explaination 
Create 2 communities and add 6 published articles in each community. Add 3
users to the system. All this will be done by django admin. The first user will join
community 1 and the second user will join community 2. Now create some views
for the articles in each community. The user in community 1 will give views to
some articles of community 1 and user 2 will do the same for community 2. Some
articles will get more views than the others in each community. For instance,
article 1 from community 1 will get 10 views, article 2 will get 8 views, article 3
will get 2 views and the left wouldn't get any new views by user1 and similarly in
community 2 by user 2. Now Login as user 3 and view articles 2,3 and 4 from
community 1. Finally, train the model.
The percentage of articles present in the recommendations list of test_user_3 should be more from the community 1 
than the  community 2.

## `.env` Varialbles:

1.  __RECOMMENDATION_SYSTEM_DOCKER_ADDRESS.__ This field is the ip address of the docker.
2.  __RECOMMENDATION_SYSTEM_NAME.__ This field is the username of any existing user in the system(prefered django admin).
3.  __RECOMMENDATION_SYSTEM_PASSWORD.__ This field is the password of above username.
4.  __RECOMMENDATION_SYSTEM_DEPLOY_ADDRESS.__ This field is the ip address of the Collaborative system (with ports).
5.  __RECOMMENDATION_SYSTEM_DJANGO_ADMIN_NAME.__ This field is the username of django admin.
6.  __RECOMMENDATION_SYSTEM_DJANGO_ADMIN_PASSWORD.__ This field is the password of django admin.
7.  __RECOMMENDATION_SYSTEM_MINIMUM_RECOMMENDATION_PERCENTAGE.__ This field is set by tester which required, the minimum percentage of test community articles 1 in the recommendation of test user 3.( default: 60% )
8. __RECOMMENDATION_SYSTEM_WEB_IP.__ This field is the IP address of the system.
9. __RECOMMENDATION_SYSTEM_WEB_PORT.__ This field is the IP address-port of the system.


## Warning
The web driver may fail. Then, in that case It is required to remove the test_community1 and test_community2,test_user1,test_user2,test_user3,test_community_article_11,....,etc (if formed, check in django admin).And then run the test_file_driver.py again.

### Note 
1. The image is kept because the selenium is creating the community and article. It is required the image file.
2. For the proper working of the test_file3, make sure , the model is trained after the execution of test_file2.py. 
