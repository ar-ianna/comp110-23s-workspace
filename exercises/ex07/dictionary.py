"""EX07 - Dictionary Functions."""
___author___ = "730488361"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, the keys & values should be inverted in another dictionary."""
    new: dict[str, str] = {}
    for key in d:
        value = d[key]
        if value in new:
            raise KeyError("Keys must be unique")
        new[value] = key
    return new


def favorite_color(d: dict[str, str]) -> str:
    """Given dictionary, returns most popular favorite color."""
    result: dict[str, int] = {}
    most_popular: str = ""
    popularity: int = 0
    for name in d:
        color = d[name]
        if color in d:
            result[color] += 1
        else:
            result[color] = 1
    for key in result:
        if result[key] > popularity:
            popularity = result[key]
            most_popular = key
    return most_popular
 

def count(list: list[str]) -> dict[str, int]:
    """Given list, dictionary is returned with how many times value appears.""" 
    result: dict[str, int] = {}
    for key in list:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result