#!/usr/bin/env python3
"""Complex types - mxed list"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Returns the sum of list of float and int"""
    return float(sum(mxd_lst))
