#!/usr/bin/env python3
"""
MRU Caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
        MRUCache class
    """
    def __init__(self):
        """
            Constructor method
        """
        super().__init__()
        # __order: used to determine most recently used. The higher
        # the index, the more recently used is the value
        self.__order = []

    def put(self, key, item):
        """
            Assign data to dictionary
        """
        if key is not None and item is not None:
            cache_data_len = len(self.cache_data)
            if cache_data_len >= self.MAX_ITEMS:
                if key in self.__order:
                    # if key already in __order, remove it and later
                    # reassign it as most recently used
                    x = self.__order.index(key)
                    del self.__order[x]
                else:
                    # if key not in __order, just remove the most recently
                    # used item and reassign new key as most recently used
                    key_to_remove = self.__order[-1]
                    del self.cache_data[key_to_remove]
                    print("DISCARD: {}".format(self.__order[-1]))
                    del self.__order[-1]
            self.__order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
            returns a value in self.cache
        """
        if key is None or key not in self.cache_data:
            return None

        # Before returning the value of key, reassign it on the mru index
        x = self.__order.index(key)
        del self.__order[x]
        self.__order.append(key)
        return self.cache_data[key]
