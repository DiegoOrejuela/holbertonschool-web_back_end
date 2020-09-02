#!/usr/bin/env python3
"""
Redis basic module
"""
from typing import Union, Callable, Optional
import redis
import uuid
from functools import wraps


def count_calls(method: callable) -> Callable:
    """
    Create and return function that increments the count
    for that key every time the method is called and returns
    the value returned by the original method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        wrapper function
        """
        self._redis.incrby(method.__qualname__, 1)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs
    for a particular function.
    """
    @wraps(method)
    def wrapper(self, *args):
        """
        wrapper function
        """
        self._redis.rpush("{}:inputs".format(method.__qualname__), str(args))
        result = method(self, *args)
        self._redis.rpush("{}:outputs".format(method.__qualname__),
                          str(result))
        return result
    return wrapper


def replay(method: Callable):
    """Displays nthe history of calls
    """
    r = redis.Redis()
    method_name = Cache.store.__qualname__

    inputs = r.lrange("{}:inputs".format(method_name), 0, -1)
    outputs = r.lrange("{}:outputs".format(method_name), 0, -1)

    print("{} was called {} times:".format(method_name,
          r.get(method_name).decode("utf-8")))
    for i, o in tuple(zip(inputs, outputs)):
        print("{}(*('{}',)) -> {}".format(method_name, i.decode("utf-8"),
              o.decode("utf-8")))


class Cache:
    """ Cache class
    """

    def __init__(self):
        """ __init __
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Takes a data argument and returns a string. The method
        should generate a random key (e.g. using uuid), store the input
        data in Redis using the random key and return the key.
        """
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """  Reading from Redis and recovering original type
        """
        value = self._redis.get(key)
        if value:
            try:
                value = fn(value)
            except Exception:
                pass
        return value
