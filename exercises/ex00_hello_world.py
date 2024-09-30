"""First COMP 110 code"""

__author__ = "730754245"


def greet(name: str) -> str:
    """A welcoming first function definition"""
    return "Hello, " + name + "!"


print(greet(name=input("What is your name?\n")))
