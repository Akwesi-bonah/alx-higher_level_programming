#!/usr/bin/python3
"""represent lookup function"""


def lookup(obj):
    """Define lookup"""
    return dir(obj)


if __name__ == "__main__":
    class MyClass1(object):
        pass


    class MyClass2(object):
        my_attr1 = 3

        def my_meth(self):
            pass


    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
