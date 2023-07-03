#!/usr/bin/python3
"""Define  a Rectangle class"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """initial a new Rectangle
        Args:
            width: define the width of the rectangle
            height: define the height of the rectangle
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """find the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        a = self.__width + self.__width
        b = self.__height + self.__height

        return a + b

    def __str__(self):
        """Printable representation of Rectangle
        print rectangle with #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ['#' * self.__width + '\n' for _ in range(self.__height)]
        return ''.join(rect).rstrip('\n')

    def __repr__(self):
        """Return string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(str(my_rectangle))
    print("--")
    print(my_rectangle)
    print("--")
    print(repr(my_rectangle))
    print("--")
    print(hex(id(my_rectangle)))
    print("--")

    # create new instance based on representation
    new_rectangle = eval(repr(my_rectangle))
    print(str(new_rectangle))
    print("--")
    print(new_rectangle)
    print("--")
    print(repr(new_rectangle))
    print("--")
    print(hex(id(new_rectangle)))
    print("--")

    print(new_rectangle is my_rectangle)
    print(type(new_rectangle) is type(my_rectangle))
