"""
This module contains a script for sending requests to mytierlist.com
"""

import concurrent.futures
import gc
import json
import random
import string
import requests

def get_random_name(length=10):
    """
    Generate a random string of fixed length.
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def get_random_number(min_l, max_l):
    """
    Generate a random number between min_l and max_l.
    """
    return random.randint(min_l, max_l)

def send_request(headers, url):
    """
    Send a request to the mytierlist vote url with the given headers.
    """
    sort_values = {}

    option_tiers = []
    for i in range(88239, 88244):
        tier = get_random_number(28193, 28197)

        if tier in sort_values:
            sort_values[tier] += 1
        else:
            sort_values[tier] = 0

        option_tiers.append({"id":i,"text":str(i-88238),"sort":sort_values[tier],"tier":tier})

    payload = {
        "nickname": get_random_name(),
        "pollId":7765592,
        "optionTiers": option_tiers
    }

    with requests.post(url, headers=headers, data=json.dumps(payload), timeout=5) as response:
        pass  # Handle the response here if needed

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://mytierlist.com/app/polls/7765592",
    "Content-Type": "application/json",
    "Origin": "https://mytierlist.com",
    "DNT": "1",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-GPC": "1"
}

URL = "https://mytierlist.com/api/polls/7765592/vote"

NUM_THREADS = 100

with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
    while True:
        executor.submit(send_request, HEADERS, URL)
        gc.collect()
