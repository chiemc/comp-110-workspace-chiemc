def sum(num1: int, num2: int) -> int:
    """Add two numbers together."""
    return num1 + num2


print(sum(num1=1, num2=10))  # <- 1 and 10 are arguments

# heap: id: 0 fn 1-3
# stack: globals, sum id: 0|sum, return address: 6, same line you call your function
# stack/call stack: num1: 1 num2: 10
# now that you have the frames ready and called the function, you can now go in the body
# stack/call stack: return value: 11
# output: 11
