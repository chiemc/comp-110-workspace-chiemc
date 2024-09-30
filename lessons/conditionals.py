"""Practicing my conditionals."""


def less_than_10(num: int) -> None:
    """Tell us if num < 10."""
    dub: int = num * 2
    num = dub
    print(dub)
    if num < 10:  # check if this is true
        print("Small number!")  # "then" block
    else:
        print("Big number!")
    print("This is the end of the function.")


def wake_up(alarm: bool) -> str:
    if alarm is True:
        print("Wake up! Go to COMP 110!")
    else:
        print("Keep sleeping. You deserve it. :)")


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="Fifty", letter="G"))


wake_up(alarm=False)

less_than_10(num=9)
