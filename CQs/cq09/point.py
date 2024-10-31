from __future__ import annotations


"""Intro to Object Oriented Programming"""


__author__ = "730754245"


class Point:
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        self.x *= factor
        self.y *= factor
        return None

    def scale(self, factor: int) -> Point:
        new_point = Point(self.x, self.y)
        new_point.scale_by(factor)
        return new_point
