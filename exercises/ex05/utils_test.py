"""ex05 utils test"""

__author__ = "730754245"


from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens() -> None:
    """Tests that the function returns only even numbers"""
    evens: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(evens) == [2, 4, 6]


def test_only_evens_edge_case() -> None:
    """Tests the edge case of negative numbers"""
    numbers: list[int] = [-1, -2, -3, -4]
    assert only_evens(numbers) == [-2, -4]


def test_only_evens_mutation() -> None:
    """Tests that the function mutates the list properly"""
    evens: list[int] = [1, 2, 3, 4, 5, 6]
    assert len(only_evens(evens)) == 3


def test_sub() -> None:
    """Tests that the function returns elements within the given start and end index"""
    a: list[int] = [10, 20, 30, 40]
    assert sub(a, 1, 3) == [20, 30]


def test_sub_edge_case() -> None:
    """Tests the edge case of negative numbers"""
    a: list[int] = [-20, -40, -60, -80, -100]
    assert sub(a, 1, 3) == [-40, -60]


def test_sub_mutation() -> None:
    """Tests if the function mutates the list properly"""
    a: list[int] = [10, 20, 30, 40]
    assert len(sub(a, 1, 3)) == 2


def test_add_at_index() -> None:
    """Tests to see if add_at_index returns None"""
    list_1 = [1, 2, 3, 5]
    assert add_at_index(list_1, 4, 3) is None


def test_add_at_index_mutation() -> None:
    """Tests to see if add_at_index mutates the list"""
    list_1 = [1, 2, 3, 5]
    add_at_index(list_1, 4, 3)
    assert list_1 == [1, 2, 3, 4, 5]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    list_3 = []
    with pytest.raises(IndexError):
        add_at_index(list_3, 1, 1)
        # an IndexError is raised for the case
        # when the add_at_index is given an <index_to_insert_num>
        # that is greater than the length of our <list_object>
