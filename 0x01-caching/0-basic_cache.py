#!/usr/bin/env python3
"""
  BasicCache - a class that inherits from BaseCaching
  and is a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
        Class Basic Cache
        inherits from BaseCaching
    """

    def __init__(self):
        """
            The constructor function of BasicCache
        """
        super().__init__()

    def put(self, key, item):
        """
            Assign key value pair to cache variable
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """
            Return the value in self.cache_data linked to key
        """
        if key is None:
            return None
        if key not in self.cache_data:
            return None
        return self.cache_data[key]
