def factorial(n: int) -> int:
    """Calculates positive factorial of int n."""
    if n < 0:
        raise ValueError("N must be a positive integer")
    if n == 0 or n == 1:
        return 1
    else:
        product = n - 1
        return n * factorial(product)


print(factorial(5))
