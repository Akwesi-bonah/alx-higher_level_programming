#!/usr/bin/python3
"""Represent rectangle the inherit base class"""
from models.base import Base


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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be >= 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

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
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get value for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set value for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
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
        if args is not None and kwargs is not None:
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
            return
        return self.__init__(self.width,
                             self.height, self.x, self.y)

    def to_dictionary(self):
        """Rectangle instance to dictionary representation"""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }

    def __str__(self):
        """string representation of the rectangle"""
        result = f'[{Rectangle.__name__}] ({self.id}) '
        result += f'{self.x}/{self.y} - {self.width}/{self.height}'
        return result

