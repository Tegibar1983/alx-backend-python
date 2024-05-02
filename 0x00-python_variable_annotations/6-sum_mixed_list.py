#!/usr/bin/env python3

""" A function that computes the sum of 2 mixed type nums and return sum as float
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return float(sum(mxd_lst))
