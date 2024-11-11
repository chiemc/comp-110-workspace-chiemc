"""File to define Bear class."""


class Bear:
    """Bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializing attributes for Bear."""
        self.age: int = 0
        self.hunger_score: int = 0
        return None

    def one_day(self):
        """Increases age by one and decreases hunger score by one."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Updates the Bear's hunger_score so that it increases by num_fish."""
        adjusted_hunger_score: int = 0
        while adjusted_hunger_score < num_fish:
            adjusted_hunger_score += 1
        self.hunger_score += adjusted_hunger_score
