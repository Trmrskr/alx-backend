#!/usr/bin/env python3
"""
    LFRU Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
        LFUCache class
    """
    def __init__(self):
        """
        Constructor method
        """
        super().__init__()
        self.__frequency = {}
        self.__order = []

    def put(self, key, item):
        """
            puts value into cache
        """
        if key is not None and item is not None:
            cache_data_len = len(self.cache_data)
            if cache_data_len >= self.MAX_ITEMS:
                if key in self.__order:
                    x = self.__order.index(key)
                    del self.__order[x]
                else:
                    lst = min(self.__frequency.values())
                    lru = [k for k, v in self.__frequency.items() if v == lst]
                    lru_idx = min([self.__order.index(k) for k in lru])
                    lru_key = self.__order[lru_idx]
                    del self.cache_data[lru_key]
                    print("DISCARD {}".format(lru_key))
                    del self.__order[lru_idx]
                    del self.__frequency[lru_key]

            self.__order.append(key)
            self.cache_data[key] = item
            if key in self.__frequency:
                self.__frequency[key] += 1
            else:
                self.__frequency[key] = 1

    def get(self, key):
        """
            Get the value of a given key
        """
        if key is None or key not in self.cache_data:
            return None

        x = self.__order.index(key)
        del self.__order[x]
        self.__order.append(key)
        self.__frequency[key] += 1
        return self.cache_data[key]
