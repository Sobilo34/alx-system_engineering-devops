#!/usr/bin/python3
"""
A function that queries the Reddit API and
returns number id subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    function that calculate the subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    response = requests.get(url.format(subreddit), headers=headers,
                            allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data', {}).get('subscribers', 0)
    else:
        return 0
