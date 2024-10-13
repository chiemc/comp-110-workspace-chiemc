"""list Utility Functions exercise"""

__author__ = "730754245"


def all(numbers: list[int], single: int) -> bool:
    """Determines if all of the ints in the list are the same as the given int"""
    match: int = 0
    # match variable to track matching ints
    for elem in numbers:
        if single == elem:
            match += 1
    if match != len(numbers) or numbers == []:
        # use or to combine both conditionals for efficiency
        return False
    else:
        return True


def max(numbers: list[int]) -> int:
    """Outputs the largest int in the list"""
    largest_number: int = numbers[0]
    # variable to track largest number in list, intialize with numbers[0] instead of 0
    # covers edge case of negatives
    if len(numbers) == 0:
        raise ValueError("max() arg is an empty List")
    for elem in numbers:
        if elem > largest_number:
            largest_number = elem
        # if elem > largest_number, largest_number takes on that value
    return largest_number


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Determines if two lists are identical or not"""
    match: str = ""
    match2: str = ""
    # two variables to track the elements in each list
    for elem in list1:
        match += str(elem)
    for numbers in list2:
        match2 += str(numbers)
    if match == match2:
        return True
    else:
        return False


def extend(list3: list[int], list4: list[int]) -> None:
    """Takes two lists and mutates one by appending the other to it"""
    for elem in list4:
        list3.append(elem)
    # append each elem in list 4 to list 3 via for loop
    return None
