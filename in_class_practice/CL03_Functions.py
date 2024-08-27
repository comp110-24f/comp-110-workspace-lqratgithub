"""Practice with functions."""

from random import randint

print(randint(1, 10))


# Function Definition
def sum(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b


# Function Call
print(sum(a=2, b=13))
