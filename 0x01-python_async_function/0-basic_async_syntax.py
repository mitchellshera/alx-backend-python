#!/usr/bin/env python3
''' Task 0 module '''


import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.
    
    :param max_delay: Maximum delay in seconds (default is 10).
    :return: The random delay.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
