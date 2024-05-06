#!/usr/bin/env python3

'''Asyncio Function
'''

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    '''
    Asyncio function  named wait_random with 2 params named  max_delay and int 10
    '''

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

