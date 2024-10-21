def find_and_remove_max(numbers: list[int]) -> int:
    """Returns and removes the largest number in the list"""
    if numbers == []:
        return -1
    largest_number: int = numbers[0]
    for elem in numbers:
        if elem > largest_number:
            largest_number = elem
    idx: int = 0
    while idx < len(numbers):
        if numbers[idx] == largest_number:
            numbers.pop(idx)
        else:
            idx += 1
    return largest_number


a: list[int] = [1, 2, 3, 3]
find_and_remove_max(a)
print(a)
