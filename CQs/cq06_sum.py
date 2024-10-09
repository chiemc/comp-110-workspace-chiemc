"""Summing the elements of a list using different loops"""

__author__ = "730754245"


def w_sum(vals: list[float]) -> float:
    idx: int = 0
    total: float = 0.0
    while idx < len(vals):
        total += vals[idx]
        idx += 1
    return total


def f_sum(vals: list[float]) -> float:
    total: float = 0.0
    for numbers in vals:
        total += numbers
    return total


def f_range_sum(vals: list[float]) -> float:
    total: float = 0.0
    for numbers in range(0, len(vals)):
        total += vals[numbers]
    return total
