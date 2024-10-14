#!/usr/bin/env python3
"""
Module that contains an asynchronous coroutine that takes in an integer as
argument (max_delay, with a default value of 10) named wait_random that waits
for a random delay between 0 and max_delay (included and float value) seconds
and eventually returns it.
"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine that takes in an integer as
    argument (max_delay, with a default value of 10) named wait_random that
    waits for a random delay between 0 and max_delay (included and float value)
    seconds and eventually returns it.
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
