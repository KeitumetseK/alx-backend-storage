#!/usr/bin/env python3
"""
Web cache and URL access tracker using Redis.
"""

import redis
import requests
from typing import Callable
from functools import wraps

r = redis.Redis()

def count_access(method: Callable) -> Callable:
    """
    Decorator to count how many times a particular URL is accessed.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Increment the count for the URL access and call the original method.
        """
        key = f"count:{url}"
        r.incr(key)
        return method(url)
    return wrapper

@count_access
def get_page(url: str) -> str:
    """
    Obtain the HTML content of a URL and cache it with an expiration time of 10 seconds.

    Args:
        url (str): The URL to retrieve.

    Returns:
        str: The HTML content of the URL.
    """
    cache_key = f"cached:{url}"
    cached_content = r.get(cache_key)
    
    if cached_content:
        return cached_content.decode("utf-8")

    response = requests.get(url)
    r.setex(cache_key, 10, response.text)
    return response.text

# Example usage
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"
    print(get_page(url))  # Fetches and caches the content
    print(get_page(url))  # Returns cached content

