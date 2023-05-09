#!/usr/bin/python3
"""
number_of_subscribers(subreddit) query the reddit api,
returns the number of subscribers
or 0 if subreddit is invalid
"""

import requests


def number_of_subscribers(subreddit):
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get(f'http://www.reddit.com/r/{subreddit}/about.json',
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'}).json()
    subscribers = r.get("data", {}).get("subscribers", 0)
    return subscribers
