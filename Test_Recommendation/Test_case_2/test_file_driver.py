import os
import time
from decouple import config

os.system("python3 test_file1.py")
os.system("python3 test_file2.py")
os.system("curl -i -X POST -H 'Content-Type: application/json' -d '{\"article-view\": \"http://"+config("RECOMMENDATION_SYSTEM_WEB_IP")+":"+config("RECOMMENDATION_SYSTEM_WEB_PORT")+"/logapi/event/article/view\", \"debug\": \"True\"}' http://localhost:3445/train")
print("Training the model")
time.sleep(20)
print("Model has been trained")
os.system("python3 test_file3.py")
os.system("python3 test_file4.py")
