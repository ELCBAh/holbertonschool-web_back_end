#!/usr/bin/env python3
"""
async coroutine that takes int as argument and returns float
"""
import asyncio
from typing import Generator


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay."""
    return max_delay
