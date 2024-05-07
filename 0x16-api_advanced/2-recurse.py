#!/usr/bin/python3
"""
Recursively queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    This is the function
    """
    url = "https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'limit': 100, 'after': None}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        if len(posts) == 0:
            if len(hot_list) == 0:
                return None
            else:
                return hot_list
        else:
            for post in posts:
                hot_list.append(post['data']['title'])
            params['after'] = data['data']['after']
            return recurse(subreddit, hot_list)
    else:
        return None
