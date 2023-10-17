import requests
import gc
from concurrent.futures import ThreadPoolExecutor

def fetch_data(url, header):
    """
    Fetch data from a URL using an HTTP GET request.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        str: The response text.
    """
    with requests.get(url, headers=header, timeout=10) as request:
        pass

HEADER = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://mytierlist.com/app/polls/7765592/result',
        'Content-Type': 'application/json',
        'DNT': '1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
        'TE': 'trailers',
    }

URL = "https://mytierlist.com/api/polls/7765592/votes"

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=20) as executor:
        while True:
            executor.submit(fetch_data, URL, HEADER)
            gc.collect()
