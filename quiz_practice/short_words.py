"""Short Words Practice for QZ02."""
___author___ = "730488361"


def short_words(my_list: list[str]) -> list[str]:
    """Return list of words shorter than 5 characters."""
    new_words: list[str] = []
    for word in my_list:
        if len(word) < 5:
            new_words.append(word)
        else:
            print(f"{word} is too long!")
    return new_words