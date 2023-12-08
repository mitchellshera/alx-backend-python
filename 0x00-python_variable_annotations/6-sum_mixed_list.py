#!/usr/bin/env python3
'''Task 6 module'''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Computes the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The
        input list of integers and floats.

    Returns:
        float: The sum of the input list elements.
    """
    return sum(mxd_lst)
