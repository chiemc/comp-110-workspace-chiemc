from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first() -> None:
    """Test that get first returns first element"""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert get_first(fruits) == "apples"


def test_remove_first() -> None:
    """Test that remove_first returns None"""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert remove_first(fruits) is None
    # can use == None or is None


def test_remove_first_behavior() -> None:
    """Test the behavior/mutation of remove first"""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    remove_first(fruits)
    assert fruits == ["oranges", "bananas"]


def test_get_and_remove_first() -> None:
    """Test that get and remove first removes first element and returns it"""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert get_and_remove_first(fruits) == "apples"


def test_get_first_edge_case() -> None:
    """Test that get first works with empty list"""
    input: list[str] = []
    assert get_first(input) == ""
