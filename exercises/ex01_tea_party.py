"""Tea Party Program"""

__author__: str = "730754245"


def main_planner(people: int) -> None:
    """Main function that calls each function"""
    print("A Cozy Tea Party for", people, "people!")
    print("Tea Bags:", tea_bags(people))  # must call the function AND the parameter
    print("Treats:", treats(people))  # calculate calculate calculate math
    print(f"Cost: ${cost(tea_bags(people), treats(people))}")
    # only way i could close the whitespace between $ and the result of cost()


def tea_bags(people: int) -> int:
    """Determines the number of guests attending the tea party."""
    return people * 2  # assumes that each guest will have 2 tea bags


def treats(people: int) -> int:
    """Computes the number of treats needed based on how many guests are drinking."""
    return int(tea_bags(people=people) * 1.5)
    # guests will want this amount of treats


def cost(tea_count: int, treat_count: int) -> float:
    """Computes the cost of the tea bags and treats"""
    return tea_count * 0.50 + treat_count * 0.75
    # multiplies by the cost and adds them together


if __name__ == "__main__":
    main_planner(people=int(input("How many guests are attending your tea party?\n")))
    # use input when needing a user's input on something, and use \n for line break
