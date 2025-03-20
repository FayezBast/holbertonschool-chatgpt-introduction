
#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer `n` recursively.

    Parameters:
    n (int): The non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input integer `n`.
         Returns 1 if `n` is 0 (0! = 1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read an integer from command-line arguments and compute its factorial
f = factorial(int(sys.argv[1]))
print(f)

