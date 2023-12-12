#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime and return it"""
    s = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    elapsed = time.perf_counter() - s

    return elapsed
