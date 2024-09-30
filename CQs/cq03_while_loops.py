"""While loop challenge question"""

__author__ = "730754245"


def num_instances(phrase: str, search_char: str) -> None:
    count: int = 0
    index_track: int = 0
    while index_track < len(phrase):
        if search_char == phrase[index_track]:
            count += 1
        index_track += 1
    print(count)


num_instances(phrase=input("Enter a phrase:"), search_char=input("Enter a character:"))
