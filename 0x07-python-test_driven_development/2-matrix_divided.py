#!/usr/bin/python3

"""Represent a function that divide as element of a matrix"""


def matrix_divided(matrix, div):
    """Divide all element in a matrix
    Args:
        matrix (list):  list of integer or float values
        div (int/float): the divisor

    Raises:
        TypeError: if the element is not integer or float
        TypeError: If the matrix contains rows of different sizes
        TypeError: if the divisor is not an integer or flaot value
        ZeroDivisionError: if the divisor is zero

    Returns: New matrix of the result
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(value, int) or isinstance(value, float))
                    for value in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
    return result


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)

