#!/usr/bin/python
# -*- coding: utf-8 -*-

'''Write a function that queries the Reddit API
and prints the titles of the first 10 hot posts
listed for a given subreddit.'''

import json
import requests


def top_ten(subreddit):
    '''function to check top then of sub.'''

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_Agent = 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'

    headers = {'User-Agent': user_Agent}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    response_data = response.json()
    for data in (response_data['data']['children'])[:10]:
        print(data['data']['title'])
