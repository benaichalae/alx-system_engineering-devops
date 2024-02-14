#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
    return 0
