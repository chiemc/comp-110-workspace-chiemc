"""Testing find_max"""

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max() -> None:
    numbers: list[int] = [1, 2, 4, 3, 4]
    assert find_and_remove_max(numbers) == 4


def test_find_and_remove_max_mutation() -> None:
    numbers: list[int] = [1, 8, 2, 3, 3]
    find_and_remove_max(numbers)
    assert numbers == [1, 2, 3, 3]


def test_find_and_remove_max_edge_case() -> None:
    blank: list[int] = []
    assert find_and_remove_max(blank) == -1
