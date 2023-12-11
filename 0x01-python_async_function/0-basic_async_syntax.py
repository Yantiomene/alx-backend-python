#!/usr/bin/env python3
"""The Basics of async"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay"""
    wait_delay = random.random() * max_delay
    await asyncio.sleep(wait_delay)
    return wait_delay
