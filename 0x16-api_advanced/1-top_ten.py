#!/usr/bin/python3
"""
queries the Reddit API; prints the titles of the first 10 hot posts
"""
import requests
import sys


def top_ten(subreddit):
    """
        return top ten titles for a given subreddit
        return None if invalid subreddit given
    """
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    r = requests.get(url, headers=headers).json()
    top_ten = r.get('data', {}).get('children', [])
    if not top_ten:
        print(None)
    for t in top_ten:
        print(t.get('data').get('title'))
