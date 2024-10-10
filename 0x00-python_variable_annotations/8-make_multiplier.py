#!/usr/bin/env python3
"""
Type-annotated function make_multiplier
Returns a function that multiplies the float
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Type-annotated function make_multiplier
    Returns a function that multiplies the float
    """
    return lambda x: x * multiplier
