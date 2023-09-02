#!/usr/bin/env python3
"""
a coroutine called async_generator that will loop 10 times
"""
import asyncio
import random
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[Float]:
    """
    Coroutine that will loop 10 times, each time asynchronously wait 1 second
    then yield a random number between 0 and 10.
    """
    return [i async for i in async_generator()]
