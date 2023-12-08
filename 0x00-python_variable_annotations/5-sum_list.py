#!/usr/bin/env python3
'''Task 5 module'''


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Computes the sum of a list of floats.

    Args:
        input_list (List[float]): The input list of floats.

    Returns:
        float: The sum of the input list elements.
    """
    return sum(input_list)
