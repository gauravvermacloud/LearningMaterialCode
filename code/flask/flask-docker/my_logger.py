from functools import wraps
import inspect
import threading


def wrap():
    """ Wrapper """
    def decorate(func):
        """ Decorator """
        def call(*args, **kwargs):
            """ Actual wrapping """
            current_thrd = threading.currentThread()
            print(current_thrd.ident)
            if(hasattr(current_thrd,"my_prop")):    
                print(current_thrd.my_prop)
            entering(func)
            result = func(*args, **kwargs)
            exiting(func)
            return result
        return call
    return decorate


def entering(func):
    """ Pre function logging """
    print("entering function ==============> "+func.__name__)
    source = inspect.getsource(func)
    index = source.find("def ")
    decs = [
        line.strip().split()[0]
        for line in source[:index].strip().splitlines()
        if line.strip()[0] == "@"
    ]
    route = [r for r in decs if "route" in r]
    print(route)


def exiting(func):
    """ Post function logging """
    print("exiting function ==============> "+func.__name__)

# https://towardsdatascience.com/using-wrappers-to-log-in-python-ccffe4c46b54
