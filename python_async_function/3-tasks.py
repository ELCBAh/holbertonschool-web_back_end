#!/usr/bin/env python3
"""
takes integer max_delay and returns the time it takes to execute
"""
import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    task_wait_random function
    """
    return asyncio.create_task(wait_random(max_delay))
