#!/usr/bin/python3
"""
Recursively queries the Reddit API, parses the titles of all hot articles,
and prints a sorted count of given keywords.
"""
from requests import get


def count_words(subreddit, word_list, word_count=[], page_after=None):
    """
    This is the function
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    word_list = [word.lower() for word in word_list]

    if bool(word_count) is False:
        for word in word_list:
            word_count.append(0)

    if page_after is None:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        data = get(url, headers=headers, allow_redirects=False)
        if data.status_code == 200:
            for child in data.json()['data']['children']:
                i = 0
                for i in range(len(word_list)):
                    for word in [w for w in child['data']['title'].split()]:
                        word = word.lower()
                        if word_list[i] == word:
                            word_count[i] += 1
                    i += 1

            if data.json()['data']['after'] is not None:
                count_words(subreddit, word_list,
                            word_count, data.json()['data']['after'])
    else:
        url = ('https://www.reddit.com/r/{}/hot.json?after={}'
               .format(subreddit,
                       page_after))

        data = get(url, headers=headers, allow_redirects=False)

        if data.status_code == 200:
            for child in data.json()['data']['children']:
                i = 0
                for i in range(len(word_list)):
                    for word in [w for w in child['data']['title'].split()]:
                        word = word.lower()
                        if word_list[i] == word:
                            word_count[i] += 1
                    i += 1
            if data.json()['data']['after'] is not None:
                count_words(subreddit, word_list,
                            word_count, data.json()['data']['after'])
            else:
                dicto = {}
                for key_word in list(set(word_list)):
                    i = word_list.index(key_word)
                    if word_count[i] != 0:
                        dicto[word_list[i]] = (word_count[i] *
                                               word_list.count(word_list[i]))

                for key, value in sorted(dicto.items(),
                                         key=lambda x: (-x[1], x[0])):
                    print('{}: {}'.format(key, value))