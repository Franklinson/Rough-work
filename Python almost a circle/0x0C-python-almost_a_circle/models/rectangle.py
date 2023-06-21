#!/usr/bin/python3

from models.base import Base
"""Importing the model base from models.base"""


class Rectangle(Base):
    """A class called Rectangle is created from base model"""

    def __init__(self, width, height, x = 0, y = 0, id= None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if input(value) != int:
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be > 0")
        return self.__width == value
        
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if input(value) != int:
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be > 0")
        return self.__height == value
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def width(self, value):
        if input(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        return self.__x == value
        
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        if input(value) != int:
            raise TypeError("Y must be an integer")
        if value < 0:
            raise ValueError("Y must be >= 0")
        return self.__y == value
    
    def area(self):
        return self.height * self.width
    
    def display(self):
        if self.height == 0 or self.width == 0:
            print("")
            return