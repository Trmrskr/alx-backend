#!/usr/bin/env python3
"""
Simple helper function
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    returns the index_range of a page
    """
    start_index = (page * page_size) - page_size
    end_index = page_size * page
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        method takes 2 integer arguments and returns page content
        """
        assert isinstance(page_size, int) and isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        dataset = self.dataset()
        dataset_length = len(dataset)
        idx_range = index_range(page, page_size)

        total_pages = math.ceil(dataset_length/page_size)

        if page > total_pages:
            return []

        return dataset[idx_range[0]:idx_range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        returns a dictionary of page properties
        """

        data = self.get_page(page, page_size)
        data_set = self.dataset()
        total_pages = math.ceil(len(data_set)/page_size)
        next_page = page+1 if page < total_pages else None
        prev_page = page-1 if page != 1 else None

        hyper = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

        return hyper
