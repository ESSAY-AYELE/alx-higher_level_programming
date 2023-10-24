#!/usr/bin/python3

""" what ever """


class Square:
    """ class whaeve"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """getter method"""
        return self.__size

    def area(self):
        """ computes the area of square """
        return (self.__size ** 2)

    @size.setter
    def size(self, size):
        """ setter method"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """prints a square using #"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print("")
