#!/user/bin/env python3

""" Annotative function named sum_list that takes input_list as function argument """

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Computes the sum of a list of floating-point numbers.
    '''
    return float(sum(input_list))
