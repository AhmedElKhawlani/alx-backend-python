#!/usr/bin/env python3

"""
Module that defines a function that takes a string and a number
and returns a tuple that contains the string and the square of the number
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Module that defines a function that takes a string and a number
    and returns a tuple that contains the string and the square of the number
    """

    return (k, v ** 2)
