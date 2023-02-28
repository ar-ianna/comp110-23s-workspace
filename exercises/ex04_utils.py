"""EX04 - 'list' Utility Functions."""
___author___ = "730488361"

def all(a: list[int], b: int) -> bool:
    """Test if given int is the same as all in list."""
    i: int = 0
    while i < len(a):
        if b != a[i]:
            return False
        i += 1
    return True

def max(input: list[int]) -> int:
    """Return largest int in list."""
    i: int = 0
    largest: int = 0
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    while i < len(input):
        if largest < input[i]:
            largest = input[i]
            i += 1
        elif largest > input[i]:
            i += 1
    return largest
       
        
def is_equal(x: list[int], y: list[int]) -> bool:
    """Test if lists are equal to each other."""
    i: int = 0
    while i < len(x) and i < len(y):
        if x[i] != y[i] or len(x) != len(y):
            return False
        i += 1
    return True