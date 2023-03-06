"""EX05 - 'list' Utility Functions Part 2"""
___author___ = "730488361"

from exercises.ex05.utils import only_evens, sub, concat

def test_empty() -> None:
    assert only_evens([]) == []

def test_negatives() -> None:
    test_list: list[int] = [7, 6, -2, 3]
    assert only_evens(test_list) == [6, -2]

def test_only_negatives() -> None:
    test_list: list[int] = [-10, -9, -8, -7]
    assert only_evens(test_list) == [-10, -8]


def test_empty_lists() -> None:
    list_a: list[int] = []
    list_b: list[int] = []
    assert concat(list_a, list_b) == []

def test_uneven_lists() -> None:
    list_a: list[int] = [1, 2, 3]
    list_b: list[int] = [4, 5]
    assert concat(list_a, list_b) == [1, 2, 3, 4, 5]

def test_all_zeros() -> None:
    list_a: list[int] = [0, 0, 0, 0]
    list_b: list[int] = [0, 0, 0, 0]
    assert concat(list_a, list_b) == [0, 0, 0, 0, 0, 0, 0, 0]


def test_no_indexes() -> None:
    test_list: list[int] = []
    start: int = 0
    end: int = 7
    assert sub(test_list, start, end) == []

def test_large_end() -> None:
    test_list: list[int] = [1, 2, 3, 4, 5]
    start: int = -1
    end: int = 3
    assert sub(test_list, start, end) == [1, 2, 3]

def test_greater_start() -> None:
    test_list: list[int] = [2, 4, 6, 8, 10]
    start: int = 7
    end: int = 10
    assert sub(test_list, start, end) == []