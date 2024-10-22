"""EX05 list Utility Functions"""

__author__ = "730754245"


def only_evens(numbers: list[int]) -> list[int]:
    evens: list[int] = []
    for elem in numbers:
        if elem % 2 == 0:
            evens.append(elem)
    return evens


def sub(numbers: list[int], start_index: int, end_index: int) -> list[int]:
    sub_set: list[int] = []
    if start_index < 0:
        start_index = 0
    if end_index > len(numbers):
        end_index = len(numbers)
    if len(numbers) == 0 or start_index >= len(numbers) or end_index <= 0:
        return numbers
    for elem in range(start_index, end_index):
        # range incldues start_index but NOT end_index, no need to decrement end_index
        sub_set.append(numbers[elem])
    return sub_set


def add_at_index(numbers: list[int], add_element: int, desired_index: int) -> None:
    if desired_index < 0 or desired_index > len(numbers):
        raise IndexError("Index is out of bounds for the input list")
    numbers.append(add_element)
    
    numbers[desired_index] = add_element
    return None
