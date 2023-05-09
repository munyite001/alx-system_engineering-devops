#!/usr/bin/python3
"""
number_of_subscribers(subreddit) query the reddit api,
returns the number of subscribers
or 0 if subreddit is invalid
"""

import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except ValueError:
        return 0
