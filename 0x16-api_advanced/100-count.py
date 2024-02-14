#!/usr/bin/python3
"""
function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    url = "https://www.reddit.com/r/{}/hot.json?limit=100"
    if after:
        url += "&after={after}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    counts[word.lower()] = counts.get(word.lower(), 0) + title.count(word.lower())

        after = data['data'].get('after')
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        return
