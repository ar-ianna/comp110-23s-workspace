"""EX05 - 'list' Utility Functions."""
___author___ = "730488361"


def only_evens(a: list[int]) -> list[int]:
    """Given a list, return only evens."""
    evens: list[int] = list()
    i: int = 0
    while i < len(a):
        if a[i] % 2 != 1:
            evens.append(a[i])
        i += 1
    return evens


def concat(x: list[int], y: list[int]) -> list[int]:
    """Given 2 lists, all of the elements should appear in order in one list."""
    all: list[int] = list()
    xi: int = 0
    yi: int = 0
    while xi < len(x):
        all.append(x[xi])
        xi += 1
    while yi < len(y):
        all.append(y[yi])
        yi += 1
    return all


def sub(a_list: list[int], s: int, t: int) -> list[int]:
    """Given a list & start/end indexes, a list of numbers between them will return."""
    within: list[int] = list()
    i_one: int = s
    i_two: int = t
    if i_one < 0:
        i_one = 0
    if i_two > len(a_list):
        i_two = len(a_list)
    while i_one < i_two:
        if len(a_list) == 0 or i_one >= len(a_list) or i_two <= 0:
            within = []
        else:
            within.append(a_list[i_one])
            i_one += 1
    return within
