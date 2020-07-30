#!/usr/bin/env python3.7
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
        assert index >= 0 and index < len(self.__indexed_dataset)

        data = []
        next_index = None
        i = 0

        for k, v in self.__indexed_dataset.items():

            if self.__indexed_dataset.get(index):
                if k == index:
                    data.append(v)
                    j = k
                    i = k
                elif k > index:
                    if i < (j + page_size):
                        data.append(v)
                    elif i == (j + page_size):
                        next_index = k
                        break
            else:
                if i >= index and i < (index + page_size):
                    data.append(v)
                elif i == (index + page_size):
                    next_index = k
                    break

            i += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
