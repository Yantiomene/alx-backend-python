#!/usr/bin/env python3
"""Complex types - mxed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """Returns the sum of list of float and int"""
    return float(sum(mxd_lst))
