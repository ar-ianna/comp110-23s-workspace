"""Value exists practice for QZ02."""
___author___ = "730488361"


def value_exists(test_dict: dict[str, int], test_val: int) -> bool:
    """Return true if num in in dict."""
    for letter in test_dict:
        if test_val == test_dict[letter]:
                return True
    return False