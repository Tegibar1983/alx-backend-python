#!/usr/bin/env python3

'''The Basics of Async 
'''

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    
    '''
    waits for a random delay between 0 and max_delay in second and eventually returns float
    '''
    
  delay = random.uniform(0, max_delay)
  await asyncio.sleep(delay)
  return delay
