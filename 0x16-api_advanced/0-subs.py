#!/usr/bin/python3
"""
A function that queries the Reddit API and
returns number id subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Parameters:
    subreddit (str): The subreddit to query.

    Returns:
        int: Number of subscribers for given subreddit
        or 0 if subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    response = requests.get(url.format(subreddit), headers=headers)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers', 0)
    else:
        return 0
