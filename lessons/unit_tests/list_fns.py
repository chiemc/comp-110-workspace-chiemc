def get_first(words: list[str]) -> str:
    """Takes a list[str] as input and returns first element"""
    if len(words) == 0:
        return ""
    # modify code to cover edge case of empty list
    return words[0]


def remove_first(words: list[str]) -> None:
    """Takes a list[str] as input and removes first element"""
    words.pop(0)


def get_and_remove_first(words: list[str]) -> str:
    """Remove AND return first element"""
    first_elem: str = words[0]
    remove_first(words)
    return first_elem
