#!/usr/bin/env python3
'''Task 3 module '''


import asyncio
from typing import Any


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    """
    Regular function that returns an asyncio.Task for wait_random.

    :param max_delay: Maximum delay in seconds for wait_random.
    :return: asyncio.Task
    """
    # Use asyncio.create_task to create a Task for wait_random
    task = asyncio.create_task(wait_random(max_delay))
    return task
