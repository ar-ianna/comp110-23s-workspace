"""Challenge Question 4"""

def zip(a: list[str], b: list[int]) -> dict[str,int]:
    """Make dict where a is keys and b is values"""
    new_dict: dict[str, int] = {}
    i: int = 0
    if len(a) != len(b):
        return new_dict
    else:
        while i < len(a):
            new_dict[a[i]] = b[i]
            i += 1
        return new_dict
