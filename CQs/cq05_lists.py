"""Mutating Functions."""

__author__ = "730754245"


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(numbers: list[int], number: int) -> None:
    numbers.append(number)
    return None


def double(doubler: list[int]) -> None:
    index_tracker: int = 0
    while index_tracker < len(doubler):
        doubler[index_tracker] *= 2
        index_tracker += 1
    return None


double(list_2)
print(list_1)
print(list_2)
# list_1 and list_2 will output the same thing
# pretty sure its bc list_1 is just a reference to the list and
# whatever changes are made to list_2, will also be made in list_1
