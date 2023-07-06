#!/usr/bin/python3
"""Define a function that print square"""


def print_square(size):
    """
    represent square function
    Args:
        size: The of the square to be printed

    Raises:
        TypeError: if the size is not of integer type
        TypeError: if the size is less than and not of int type
        ValueError: if the size is less than zero
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(1, size + 1):
        print("#" * size)


if __name__ == "__main__":
    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")