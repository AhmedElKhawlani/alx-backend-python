#!/usr/bin/env python3
"""
Module that imports from the previous file, wait_n().
The module creates a measure_time function with integers n and max_delay as
arguments that measures the total execution time for wait_n(n, max_delay),
and returns total_time / n.
"""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Returns total execution time
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return (total_time/n)
