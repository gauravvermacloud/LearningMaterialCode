from functools import wraps
import inspect


def wrap():
    """ Wrapper """
    def decorate(func):
        """ Decorator """
        def call(*args, **kwargs):
            """ Actual wrapping """
            entering(func)
            result = func(*args, **kwargs)
            exiting(func)
            return result
        return call
    return decorate


def entering(func):
    """ Pre function logging """
    print("entering function ==============> "+func.__name__)


def exiting(func):
    """ Post function logging """
    print("exiting function ==============> "+func.__name__)

# https://towardsdatascience.com/using-wrappers-to-log-in-python-ccffe4c46b54
