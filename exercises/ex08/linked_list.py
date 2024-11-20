from __future__ import annotations

"""Ex08 linked list utils."""

__author__ = "730754245"


class Node:
    """Node class declaration."""

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        """Initialize."""
        self.value = val
        self.next = next

    def __str__(self) -> str:
        """Represent a Node object as a string."""
        rest: str = "?"
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        # Wishful thinking: Get rest of list str
        return f"{self.value} -> {rest}"


def value_at(head: Node | None, index: int) -> int:
    """Returns the value of the Node stored at the given index."""
    if head is None:
        # edge case
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        # base case
        return head.value
    else:
        return value_at(head.next, index - 1)
    # decrement the index so that it gets closer to the base case of index = 0


def max(head: Node | None) -> int:
    """Returns the max value in the linked list."""
    if head is None:
        # edge case
        raise ValueError("Cannot call max with None")
    elif head.next is None:
        # base case
        return head.value
    else:
        big: int = max(head.next)
        # can't directly using a boolean to compare head.next, so call max
        # with head.next as argument and store that in big variable
        if head.value > big:
            return head.value
        else:
            return big


def linkify(items: list[int]) -> Node | None:
    """Returns a carbon copy of a list in the form of Linked List of Nodes."""
    if items == []:
        # base case
        return None
    else:
        return Node(items[0], linkify(items[1:]))
    # creates a Node with first value in items and recursively calls linkify
    # for the rest of the list using slice


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns a linked list multiplied by a scaling factor."""
    if head is None:
        return None
    else:
        return Node(head.value * factor, scale(head.next, factor))
