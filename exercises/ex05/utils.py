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
        return []
    for elem in range(start_index, end_index):
        # range incldues start_index but NOT end_index, no need to decrement end_index
        sub_set.append(numbers[elem])
    return sub_set


def add_at_index(numbers: list[int], add_element: int, desired_index: int) -> None:
    if desired_index < 0 or desired_index > len(numbers):
        raise IndexError("Index is out of bounds for the input list")
    numbers.append(100)
    # placeholder to make space for element
    for elem in range(len(numbers) - 1, desired_index, - 1):
        # add - 1 after desired_index to signify to python to shift right
        # shifts all elements above desired_index to make space for the new element
        # start from the end of the list, shift right to higher indices
        numbers[elem] = numbers[elem - 1]
        # expressions are read right to left, not left to right chevy
    numbers[desired_index] = add_element
    return None
