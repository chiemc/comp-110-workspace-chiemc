def factorial(num: int) -> int:
    """Calculates positive factorial of int n."""
    if num < 0:
        raise ValueError("num must be a positive integer")
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(1))
print(factorial(5))
print(factorial(10))


def sum_of_natural_numbers(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)


print(sum_of_natural_numbers(5))
print(sum_of_natural_numbers(0))


def sum_of_digits(digits: int) -> int:
    """Returns the sum of digits of a number passed to the function."""
    if digits == 0:
        return 0
    return (digits % 10) + sum_of_digits(digits // 10)


def power(n: int, p: int) -> int:
    if n == 1 or p == 0:
        return 1
    return n * power(n, p - 1)


print(power(2, 3))
print(power(5, 0))
print(power(3, 4))


def gcd(q: int, r: int) -> int:
    if r == 0:
        return q
    return gcd(r, q % r)


print(gcd(48, 18))
print(gcd(56, 98))


def reverse_string(s: str) -> str:
    return reverse_helper(s, len(s) - 1)


def reverse_helper(s: str, index: int) -> str:
    if index < 0:
        return ""
    return s[index] + reverse_helper(s, index - 1)


print(reverse_string("hello"))
print(reverse_string("a"))
print(reverse_string(""))


def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
print(fibonacci(0))
print(fibonacci(6))
