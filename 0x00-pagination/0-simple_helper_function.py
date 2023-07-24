#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page, page_size):
    """
    returns the index_range of a page
    """
    if page == 0:
        return (0)
    start_index = (page * page_size) - page_size
    end_index = page_size * page
    return (start_index, end_index)
