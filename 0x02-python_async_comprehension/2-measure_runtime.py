#!/usr/bin/env python3
'''Task 2's module.
'''


import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measures the total runtime of async_
    comprehension executed four times in parallel.
    '''
    start_time = asyncio.get_event_loop().time()

    # Use asyncio.gather to execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    end_time = asyncio.get_event_loop().time()

    # Calculate and return the total runtime
    return end_time - start_time
