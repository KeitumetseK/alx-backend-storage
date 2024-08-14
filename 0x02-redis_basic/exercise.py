#!/usr/bin/env python3
"""
Cache class for interacting with Redis.
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times methods of Cache class are called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Increment the count for the method call and then call the original method.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Store input arguments and output of the method call in Redis lists.
        """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)
        return output
    return wrapper


class Cache:
    """
    Cache class to interact with Redis.
    """

    def __init__(self):
        """
        Initialize the Cache class, setting up Redis client and flushing the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis and return the generated key.

        Args:
            data (Union[str, bytes, int, float]): Data to store.

        Returns:
            str: The generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Retrieve data from Redis and optionally apply a conversion function.

        Args:
            key (str): The key to retrieve.
            fn (Optional[Callable]): Function to apply to the retrieved data.

        Returns:
            Union[str, bytes, int, float]: The retrieved data.
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieve data as a string from Redis.

        Args:
            key (str): The key to retrieve.

        Returns:
            str: The data as a string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve data as an integer from Redis.

        Args:
            key (str): The key to retrieve.

        Returns:
            int: The data as an integer.
        """
        return self.get(key, fn=int)


def replay(method: Callable) -> None:
    """
    Display the history of calls of a particular function.

    Args:
        method (Callable): The method whose history to display.
    """
    redis_instance = method.__self__._redis
    key = method.__qualname__
    inputs = redis_instance.lrange(f"{key}:inputs", 0, -1)
    outputs = redis_instance.lrange(f"{key}:outputs", 0, -1)

    print(f"{key} was called {len(inputs)} times:")
    for inp, outp in zip(inputs, outputs):
        print(f"{key}(*{inp.decode('utf-8')}) -> {outp.decode('utf-8')}")

