def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed"""
    copy: str = ""  # set up empty string and then we can copy the values over
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy += msg[index]  # copy = copy + msg[index]
        index += 1
    return copy


if __name__ == "__main__":  # if running in THIS file, will run, if import, no run
    word: str = "yoyo"  # global variable (obvi)
    print(remove_chars(word, "o"))
    print(remove_chars(word, "y"))
