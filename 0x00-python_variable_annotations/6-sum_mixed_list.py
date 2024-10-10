#!/usr/bin/env python3

"""
Module that defines a function that takes a mixed list
and returns the sum of its elements as float
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Module that defines a function that takes a mixed list
    and returns the sum of its elements as float
    """

    s: float = 0.0
    for x in mxd_lst:
        s = s + x
    return s
