"""Concatenation function"""

__author__ = "730754245"


def concat(word_1: str, word_2: str) -> str:
    print(word_1 + word_2)
    return word_1 + word_2


word1: str = "happy"
word2: str = "birthday"

if __name__ == "__main__":
    concat(word1, word2)
