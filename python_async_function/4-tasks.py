#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n. The code is nearly identical to wait_n except task_wait_random is being called.
"""
import asyncio
import random


wait_n = __import__('3-tasks').wait_n


def task_wait_n(n: int, max_delay: int) -> asyncio.Task:
    """
    task_wait_n function
    """
    return asyncio.create_task(wait_n(n, max_delay))

