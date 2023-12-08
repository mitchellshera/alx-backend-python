#!/usr/bin/env python3
'''Task 7 module'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple with the string k and the square of the int or float v.

    Args:
        k (str): The string.
        v (Union[int, float]): The int or float.

    Returns:
        Tuple[str, float]: A tuple with the string k and the square of v as a float.
    """
    return k, float(v ** 2)
