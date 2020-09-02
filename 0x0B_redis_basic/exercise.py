#!/usr/bin/env python3
"""
Redis basic module
"""
from typing import Union
import redis
import uuid


class Cache:
    """ Cache class
    """

    def __init__(self):
        """ __init __
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Takes a data argument and returns a string. The method
        should generate a random key (e.g. using uuid), store the input
        data in Redis using the random key and return the key.
        """
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key