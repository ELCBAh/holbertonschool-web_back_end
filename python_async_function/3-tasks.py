#!/usr/bin/env python3
"""
takes integer max_delay and returns the time it takes to execute
"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    task_wait_random function
    """
    return await wait_random(max_delay)
