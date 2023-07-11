#!/usr/bin/python3
"""Represent pascal triangle function"""


def pascal_triangle(n):
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row.append(prev_row[j - 1]
                           + prev_row[j])
            row.append(1)
        triangle.append(row)
    return triangle


if __name__ == "__main__":

    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
