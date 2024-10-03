"""Wordle game"""

__author__ = "730754245"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""
    turn_number: int = 1
    # number of turns is the variable to track
    while turn_number <= 6:
        print(f"=== Turn {turn_number}/6 ===")
        guess: str = input_guess(secret_word_len=len(secret))
        # assign guess to function call to store value
        answer: str = emojified(guess=guess, secret=secret)
        # assign answer to emojified to store value
        print(answer)
        if guess == secret:
            print(f"You won in {turn_number}/6 turns!")
            return None
        # using exit() deducted points, so try return None
        turn_number += 1
    if turn_number > 6:
        print("X/6 - Sorry, try again tomorrow!")


def input_guess(secret_word_len: int) -> str:
    """Takes user input and determines the length of the secret word"""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    # use the f string for convenience
    while len(guess) != secret_word_len:
        print(f"That wasn't {secret_word_len} chars! Try again: {guess}")
        guess = input(f"Enter a {secret_word_len} character word: ")
        # included guess again to change the value of guess within the while loop
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Receives a string that is expected to be one character"""
    """And another string that will be searched through for a match"""
    assert len(char_guess) == 1
    index_tracker: int = 0
    matching_character: int = 0
    while index_tracker < len(secret_word):
        if char_guess == secret_word[index_tracker]:
            matching_character += 1
        index_tracker += 1
    if matching_character > 0:
        return True
    else:
        return False
    # iterate over each index first, if match then track it, then return True or False


def emojified(guess: str, secret: str) -> str:
    """Outputs the emojis for the user"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index_tracker: int = 0
    answer: str = ""
    # answer variable to track characters and determine output
    while index_tracker < len(secret):
        if guess[index_tracker] == secret[index_tracker]:
            answer = answer + GREEN_BOX
        elif contains_char(secret_word=secret, char_guess=guess[index_tracker]):
            answer = answer + YELLOW_BOX
        else:
            answer = answer + WHITE_BOX
        index_tracker += 1
    return answer


if __name__ == "__main__":
    main(secret="python")
