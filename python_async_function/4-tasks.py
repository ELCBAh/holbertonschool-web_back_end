#!/usr/bin/env python3
"""
The code is nearly identical to wait_n except task_wait_random is being called.
"""
import asyncio
import random
from typing import List


task_wait_random = __import__('0-basic_async_syntax').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """
    task_wait_n function
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]

