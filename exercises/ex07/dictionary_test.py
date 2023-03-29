"""EX07 - Dictionary Functions Part 2."""
___author___ = "730488361"

from dictionary import invert, favorite_color, count


def test_empty() -> None:
    """Return empty dictionary when given one."""
    assert invert({}) == {}


def test_regular_invert() -> None:
    """Return dictionary with inverted keys and values from input."""
    test_dict: dict[str, str] = {"apple": "fruit", "tomato": "?", "beet": "veggie"}
    assert invert(test_dict) == {"fruit": "apple", "?": "tomato", "veggie": "beet"}


def test_regular_invert2() -> None:
    """Return dictionary with inversted ketys and values from input."""
    test_dict: dict[str, str] = {"clas": "class 1", "nsci": "class 2", "comp": "class 3", "arth": "class 4", "math": "class 5"}
    assert invert(test_dict) == {"class 1": "clas", "class 2": "nsci", "class 3": "comp", "class 4": "arth", "class 5": "math"}


def test_empty_colors() -> None:
    """Return empty string if given empty dictionary."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""


def test_regular_colors() -> None:
    """Return most popular color."""
    test_dict: dict[str, str] = {"michael": "blue", "janet": "blue", "latoya": "green", "randy": "purple"}
    assert favorite_color(test_dict) == "blue"


def test_regular_colors2() -> None:
    """Return most popular color."""
    test_dict: dict[str, str] = {"elita one": "pink", "chromia": "blue", "moonracer": "green", "firestar": "red"}
    assert favorite_color(test_dict) == "pink"


def test_empty_count() -> None:
    """Return empty dictionary if given an empty list."""   
    test_list: list[str] = []
    assert count(test_list) == {}


def test_regular_count() -> None:
    """Return dictionary with values at how many times a key was in the list."""
    test_list: list[str] = ["happy", "sad", "angry", "sad", "sleepy"]
    assert count(test_list) == {"happy": 1, "sad": 2, "angry": 1, "sleepy": 1}


def test_regular_count2() -> None:
    """Return dictionary with values at how many times a key was in the lsit."""
    test_list: list[str] = ["breakfast", "snack", "lunch", "snack", "snack", "dinner", "snack"]
    assert count(test_list) == {"breakfast": 1, "snack": 4, "lunch": 1, "dinner": 1}