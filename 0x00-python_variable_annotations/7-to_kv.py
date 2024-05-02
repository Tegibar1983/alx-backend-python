#!/usr/bin/env python3
'''Task 7's module.
'''

from typing import List, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Convert a key and its value to a Tuple.
    '''

    return (k, float(v**2))
