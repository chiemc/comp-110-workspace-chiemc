"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730754245"


def main() -> None:
    """Calls the functions together"""
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    """Takes one's input for a word and stores it for future use"""
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit(1)
        # add exit() so that the program immediately ends when something isnt right
    return word


def input_letter() -> str:
    """Takes one's input for a single character and stores it for future use"""
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character")
        exit(1)
    return letter


def contains_char(word: str, letter: str) -> None:
    """Searches for how many instances of a given character are in a given word"""
    index_track: int = 0  # also appeared in a CQ to track the index in the while loop
    matching_character: int = 0  # tracks the number of matching characters
    print("Searching for", letter, "in", word)
    while index_track < len(word):
        if letter == word[index_track]:
            print(letter, "found at index", str(index_track))
            matching_character += 1  # all of this goes on while [] is less than len
        index_track += 1  # must happen no matter what, that's why its outside the loops
    if matching_character > 0:  # determines what to print out after exiting the loop
        print(matching_character, "instances of", letter, "found in", word)
    else:
        print("No instances of", letter, "found in", word)


if __name__ == "__main__":
    main()
