#!/usr/bin/env python3
"""
Module that imports wait_random() from 0-basic_async_syntax().
The module defines a function task_wait_random() that takes an integer
max_delay and returns a asyncio.Task.
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns a asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
