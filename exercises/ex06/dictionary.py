"""EX06 dictionary"""

__author__ = "730754245"


def invert(original: dict[str, str]) -> dict[str, str]:
    switch: dict[str, str] = {}
    for key in original:
        value = original[key]
        if value in switch:
            raise KeyError
        switch[value] = key
    return switch


def favorite_color(fav: dict[str, str]) -> str:
    counter: dict[str, int] = {}
    highest_color = ""
    highest_count = 0
    for person in fav:
        color = fav[person]
        if color in counter:
            counter[color] += 1
        else:
            counter[color] = 1
        if counter[color] > highest_count:
            highest_color = color
            highest_count = counter[color]
    return highest_color


def count(list1: list[str]) -> dict[str, int]:
    key: dict[str, int] = {}
    for word in list1:
        if word in key:
            key[word] += 1
        else:
            key[word] = 1
    return key


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    key: dict[str, list[str]] = {}
    for word in list1:
        first_letter = word[0].lower()
        if first_letter in key:
            key[first_letter].append(word)
        else:
            key[first_letter] = [word]
    return key


def update_attendance(dict1: dict[str, list[str]], day: str, student: str) -> None:
    if day not in dict1:
        dict1[day] = []
    if student not in dict1[day]:
        dict1[day].append(student)
    else:
        dict1[day] = [student]
    return None
