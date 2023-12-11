#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay"""
    delays = []
    wait_delays = []

    for i in range(n):
        wait_delays.append(wait_random(max_delay))
    for wait_delay in asyncio.as_completed((wait_delays)):
        delay = await wait_delay
        delays.append(delay)

    return delays
