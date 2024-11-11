"""File to define Fish class."""


class Fish:
    """Fish class."""

    age: int

    def __init__(self):
        """Initialize attributes for Fish."""
        self.age: int = 0
        return None

    def one_day(self):
        """Increase age by one."""
        self.age += 1
        return None
