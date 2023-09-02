#!/usr/bin/env python3
"""
takes integer max_delay and returns the number of tasks executed in parallel.
"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_n function
    """
    delay_list: List[float] = []
    for _ in range(n):
        delay_list.append(await wait_random(max_delay))
    return sorted(delay_list)
