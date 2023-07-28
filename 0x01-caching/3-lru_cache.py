#!/usr/bin/env python3
"""
    LRU Cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""

    def __init__(self):
        """Constructor method"""
        super().__init__()
        # _order: ordering keys the index is proportional to the recency
        self.__order = []

    def put(self, key, item):
        """puts to cache"""
        if key is not None and item is not None:
            cache_data_len = len(self.cache_data)
            if cache_data_len >= self.MAX_ITEMS:
                if key in self.__order:
                    # Simply reassign the recency of the key
                    x = self.__order.index(key)
                    del self.__order[x]
                else:
                    # Remove the key from the order and later
                    # from the cache
                    key_to_remove = self.__order[0]
                    del self.cache_data[key_to_remove]
                    print("DISCARD: {}".format(key_to_remove))
                    del self.__order[0]

            self.__order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
            Get item from cache using key
        """
        if key is None or key not in self.cache_data:
            return None

        x = self.__order.index(key)
        del self.__order[x]
        self.__order.append(key)

        return self.cache_data[key]
