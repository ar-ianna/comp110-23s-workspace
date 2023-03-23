"""Odd & Even Practive for QZ02!"""
___author___ = "730488361"


def odd_and_even(old:list[int]) -> list[int]:
    """Return list with inputs that are odd with even index."""
    new: list[int] = []
    i: int = 0
    while i < len(old):
        if i % 2 == 0 and old[i] % 2 != 0:
                new.append(old[i])
        i += 1
    return new


            