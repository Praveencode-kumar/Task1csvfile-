import  requests
import json
import csv 

class Data_Extraction(object):
    def __init__(self):
        self.headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8'}
        self.url = "https://api.github.com/users"

    @property
    def get(self):
        try:
            result = requests.get(url=self.url, headers= self.headers, timeout=1)
            if result.ok:
                return result
            else:
                return None
        except requests.exceptions.Timeout:
            return 'Bad Response'

obj1=Data_Extraction()
print(obj1.get)


json_data = json.loads(obj1.get.text) #load the data in json format

print(json_data)

csv_data_upload = []    
for user in json_data:  
    if user["id"]%10==0: 
    
        UserLogin=user['login']
        UserName=user['login']
        FollowUrl=user['followers_url']
        Follow_url = requests.get(FollowUrl)
        followers_details = json.loads(Follow_url.text)
        followersID=[]
        followersLogin=[]
        

        for followers in followers_details:
            csv_data_upload.append([user["id"],user["login"],user["login"],followers["id"],followers['login']])

fields = ['UserId', 'UserLogin', 'UserName', 'FollowerId', 'FollowerLogin']

with open("testcase_output.csv", 'w') as file: 
    csvwriter = csv.writer(file)           
    csvwriter.writerow(fields)             
    csvwriter.writerows(csv_data_upload)   



