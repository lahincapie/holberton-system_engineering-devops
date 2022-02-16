#!/usr/bin/python3
'''python script'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    '''function to check nbre of sub'''
    response = requests.get("https://www.reddit.com/r/{}/hot.json".format(
        subreddit), headers={"User-Agent": "amine"}, params={"after": after})
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
