#!/usr/bin/env python3
"""
async coroutine that takes int as argument and returns float
"""
import asyncio
from typing import Generator
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay."""
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
