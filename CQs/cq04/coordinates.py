"""Coordinates"""

__author__ = "730754245"


def get_coords(xs: str, ys: str) -> None:
    x_index_tracker: int = 0
    y_index_tracker: int = 0
    while x_index_tracker < len(xs):
        while y_index_tracker < len(ys):
            print((xs[x_index_tracker], ys[y_index_tracker]))
            y_index_tracker += 1
        y_index_tracker = 0
        x_index_tracker += 1


if __name__ == "__main__":
    get_coords(xs="12345", ys="6789")
