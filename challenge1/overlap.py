from typing import List, Set, Any


def overlap(input_lists: list[list]) -> list:
    """Given arbitrary list of lists, calculates set overlap between all of them"""
    if len(input_lists) == 0:
        return []
    elif len(input_lists) == 1:
        return input_lists[0]
    input_as_sets: list[set[Any]] = [set(x) for x in input_lists]
    return list(input_as_sets[0].intersection(*input_as_sets))
