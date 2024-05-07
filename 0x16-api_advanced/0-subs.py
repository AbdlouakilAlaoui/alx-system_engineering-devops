#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for the number of subscribers of a subreddit.

    Args:
    subreddit (str): The subreddit to query.

    Returns:
    int: The number of subscribers if valid, 0 otherwise.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'subreddit_subscriber_counter/0.1'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check for a valid response and that we're not redirected
    if response.status_code == 200 and response.history == []:
        return response.json().get('data', {}).get('subscribers', 0)
    return 0
