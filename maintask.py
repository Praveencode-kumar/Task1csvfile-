
import requests
import json
import csv

def get_Login_user_details(login):
    single_user_details = requests.get(f'https://api.github.com/users/{login}').json()
    return single_user_details

def get_followers_details(login):
    followers_details = requests.get(f'https://api.github.com/users/{login}/followers').json()
    return followers_details

def get_all_user_details():
    user_details=requests.get(f'https://api.github.com/users').json()
    return user_details


all_user_details = get_all_user_details()
rows = []
for user in all_user_details:
    if user["id"]%5==0:
        single_user_details =get_Login_user_details(user["login"])
        followers_details = get_followers_details(single_user_details["login"])

        for followers in followers_details:
            rows.append([user["id"],user["login"],single_user_details["name"],followers["id"],followers['login']])

Userdetails = ['UserId', 'UserLogin', 'UserName', 'FollowerId', 'FollowerLogin']
filename = "output.csv"

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(Userdetails)
    csvwriter.writerows(rows)


