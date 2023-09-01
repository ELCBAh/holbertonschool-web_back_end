#!/usr/bin/env python3
"""
calls wait random n times and returns the list of all the delays
"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of all the delays (float values).
    """
    delay_list = [wait_random(max_delay) for i in range(n)]
    tasks = [asyncio.create_task(
            delay) for delay in asyncio.as_completed(delay_list)]
    return [await task for task in tasks]
