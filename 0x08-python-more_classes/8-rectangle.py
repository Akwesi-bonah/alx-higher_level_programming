#!/usr/bin/python3
"""Define  a Rectangle class"""


class Rectangle:
    """Represent a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initial a new Rectangle
        Args:
            width: define the width of the rectangle
            height: define the height of the rectangle
        """
        type(self).number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns rectangle with bigger area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):
        """Printable representation of Rectangle
        print rectangle with #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = [str(self.print_symbol) * self.__width + '\n' for _ in range(self.__height)]
        return ''.join(rect).rstrip('\n')

    def __repr__(self):
        """Return string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Return message when the class is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")


if __name__ == "__main__":
    my_rectangle_1 = Rectangle(8, 4)
    my_rectangle_2 = Rectangle(2, 3)

    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")

    my_rectangle_2.width = 10
    my_rectangle_2.height = 5
    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")
