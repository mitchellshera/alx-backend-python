#!/usr/bin/env python3
'''Task 2's module.
'''
import time
import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int,
                 max_delay: int) -> float:
    '''Measures the total execution time for wait_n(n, max_delay).

    :param n: Number of times to spawn wait_random.
    :param max_delay: Maximum delay in seconds for each wait_random.
    :return: Average execution time per wait_n call.
    '''
    start_time = time.time()

    # Run the event loop with wait_n
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    # Calculate and return the average execution time per wait_n call
    return (end_time - start_time) / n
