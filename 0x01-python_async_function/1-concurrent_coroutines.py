import asyncio
from typing import List
from random import uniform

async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay."""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous routine that spawns wait_random n times."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays

