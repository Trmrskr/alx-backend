#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns page content based on index
        """
        assert index is not None and index != 0

        # s_index - search index
        s_index = index
        idx_dataset = self.indexed_dataset()
        len_dataset = len(idx_dataset)

        assert index <= len_dataset

        while s_index not in idx_dataset:
            s_index += 1

        next_index = s_index + page_size
        # if next_index > dataset length, let data_range equal dataset length
        data_range = next_index if next_index <= len_dataset else len_dataset
        data = [idx_dataset[i] for i in range(s_index, data_range)]
        next_index = next_index if next_index <= len_dataset else None

        hyper = {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }

        return hyper
