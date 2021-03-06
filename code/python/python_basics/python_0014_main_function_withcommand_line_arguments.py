#!/usr/bin/env python3

"""This module allows addition of two numbers.
    It allows using from command line as filename.py number1, number2 
    or importintg the module
"""
import sys

def sum(x:int,y:int) ->int:
    """ Adds two numbers and returns the sum

    Args:
        x (int): The first number to be added
        y (int): The second number to be added

    Returns:
        int: The sum of two numbers
    """
    return x+y

def __print_sum__(x,y):
    """Prints the sum of two numbers

    Args:
        x (int): The first number to be added
        y (int): The second number to be added
    """
    print(sum(x,y))

if(__name__ == "__main__"):
    """Checks if the module is being run from command line
        if so it picks up the two command line arguments and
        converts them to numbers and adds them
    """
    #we are from command line
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    __print_sum__(x,y)