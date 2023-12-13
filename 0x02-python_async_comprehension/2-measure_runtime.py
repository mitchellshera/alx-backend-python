#!/usr/bin/env python3
'''Task 2's module.
'''


import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measures the total runtime of async_
    comprehension executed four times in parallel.
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
