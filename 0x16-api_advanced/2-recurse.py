#!/usr/bin/python3
'''python script'''
import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''returns a list containing the titles of all hot articles'''

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_Agent = 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'

    headers = {
        "User-Agent": user_Agent
    }

    response = requests.get(url, headers=headers, params={"after": after}, allow_redirects=False)

    if response.status_code != 200:
        return(None)
    request_data = response.json()
    after = request_data["data"]["after"]
    posts = request_data["data"]["children"]
    for post in posts:
        hot_list.append(post["data"]["title"])
    if after is not None:
        recurse(subreddit, hot_list, after)
    return(hot_list)
