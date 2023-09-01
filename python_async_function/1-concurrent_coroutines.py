#!/usr/bin/env python3
"""
calls wait random n times and returns the list of all the delays
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Returns a list of all the delays (float values).
    """
    delays = List[float]
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
