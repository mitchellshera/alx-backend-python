#!/usr/bin/env python3
'''Task 9's module'''


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each
    tuple contains an element from the input list
    and its corresponding length.

    Args:
        lst (List[str]): The input list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples,
        where each tuple contains a string
        from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
