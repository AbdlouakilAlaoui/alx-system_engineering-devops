#!/usr/bin/python3
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print("None")

if __name__ == '__main__':
    subreddit = input("Please pass an argument for the subreddit to search. ")
    top_ten(subreddit)
