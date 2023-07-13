#!/usr/bin/python3
"""Represent rectangle the inherit base class"""

Base = __import__("base").Base


class Rectangle(Base):
    """define rectangle that inherit Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialize rectangle class
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: x co-ordinate of the rectangle
            y: y co-ordinate of the rectangle
            id: id of the object
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """get for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set value for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get value for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set value for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get value for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set value for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """Get value for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set value for y"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__y = value

    def area(self):
        """return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """print the height and width"""

        if self.width == 0 or self.height == 0:
            return ""
        for _ in range(1, self.height + 1):
            [print(" ", end='') for _ in range(self.x)]
            [print('#', end='') for _ in range(self.width)]
            print('')

    def update(self, *args, **kwargs):
        """
        update the rectangle

        Args:
            *args: new values
                - 1st = id
                - 2nd = width
                - 3rd = height
                - 4th = x
                - 5th = y
        kwargs: new key pair value

        """
        if args is None:
            return self.__init__(self.width,
                                 self.height, self.x, self.y)
        if args:
            for idx, value in enumerate(args):
                match idx:
                    case 0:
                        self.id = value
                    case 1:
                        self.width = value
                    case 2:
                        self.height = value
                    case 3:
                        self.x = value
                    case 4:
                        self.y = value
        elif kwargs:
            for key, value in kwargs.items():
                match key:
                    case 'id':
                        self.id = value
                    case 'width':
                        self.width = value
                    case 'height':
                        self.height = value
                    case 'x':
                        self.x = value
                    case 'y':
                        self.y = value

    def __str__(self):
        """string representation of the rectangle"""
        result = f'[{Rectangle.__name__}] ({self.id}) '
        result += f'({self.x}/{self.y}) - {self.width}/{self.height}'
        return result


if __name__ == "__main__":

    # r1 = Rectangle(10, 2)
    # # print(r1.id)
    #
    # r2 = Rectangle(2, 10)
    # # print(r2.id)
    #
    # r3 = Rectangle(10, 2, 0, 0, 12)
    # # print(r3.id)
    #
    # r1 = Rectangle(3, 2)
    # # print(r1.area())
    #
    # r2 = Rectangle(2, 10)
    # # print(r2.area())
    #
    # r3 = Rectangle(8, 7, 0, 0, 12)
    # # print(r3.area())
    #
    # r1 = Rectangle(4, 6)
    # r1.display()
    #
    # print("---")
    #
    # r1 = Rectangle(2, 2)
    # r1.display()
    # r1 = Rectangle(4, 6, 2, 1, 12)
    # print(r1)
    #
    # r2 = Rectangle(5, 5, 1)
    # print
    # r1 = Rectangle(2, 3, 2, 2)
    # r1.display()
    #
    # print("---")
    #
    # r2 = Rectangle(3, 2, 1, 0)
    # r2.display()
    # r1 = Rectangle(10, 10, 10, 10)
    # print(r1)
    #
    # r1.update(89)
    # print(r1)
    #
    # r1.update(89, 2)
    # print(r1)
    #
    # r1.update(89, 2, 3)
    # print(r1)
    #
    # r1.update(89, 2, 3, 4)
    # print(r1)
    #
    # r1.update(89, 2, 3, 4, 5)
    # print(r1)
    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)
    pass
