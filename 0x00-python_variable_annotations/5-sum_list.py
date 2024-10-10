#!/usr/bin/env python3

"""
Module that defines a function that takes a list of floats
and returns the sum of its elements as float
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Module that defines a function that takes a list of floats
    and returns the sum of its elements
    """

    s: int = 0
    for x in input_list:
        s = s + x
    return s
