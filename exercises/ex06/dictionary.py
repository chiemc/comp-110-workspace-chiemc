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
