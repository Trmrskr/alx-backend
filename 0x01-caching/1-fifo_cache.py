#!/usr/bin/env python3
"""FIFO caching"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
        FIFOCache class
    """

    def __init__(self):
        """
            Constructor method
        """
        super().__init__()
        self.__rank = {}
        self.__rank_key = 1

    def put(self, key, item):
        """
            Assign to the dictionary
        """

        if key is not None and item is not None:

            if self.__rank_key > self.MAX_ITEMS:
                key_to_remove = min(self.__rank.keys())
                fifo_key = self.__rank.pop(key_to_remove)
                self.cache_data.pop(fifo_key)
                self.cache_data.update({key, item})
                self.__rank.update({self.__rank_key, item})
            else:
                self.cache_data.update({key, item})
                self.__rank.update({self.__rank_key: key})

            self.__rank_key += 1

    def get(self, key):
        """
            Return the value in self.cache_data linked to key
        """

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
