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
        super.__init__(id)