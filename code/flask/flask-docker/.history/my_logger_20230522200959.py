from functools import wraps
import inspect
import threading
import logging


logging.basicConfig(handlers=[
    logging.FileHandler("debug.log"),
    logging.StreamHandler()
], format='%(asctime)s ~ %(levelname)s ~  %(threadName)-12.12s ~ %(process)d ~ %(funcName)s ~ %(lineno)d ~ %(message)s', level=logging.DEBUG)


def wrap():
    """ Wrapper """
    def decorate(func):
        """ Decorator """
        def call(*args, **kwargs):
            """ Actual wrapping """
            current_thrd = threading.currentThread()
            logging.debug(current_thrd.ident)
            if (hasattr(current_thrd, "my_prop")):
                logging.debug(current_thrd.my_prop)
            entering(func)
            result = func(*args, **kwargs)
            exiting(func)
            return result
        return call
    return decorate


def entering(func):
    """ Pre function logging """
    logging.debug("entering function ==============> "+func.__name__)
    logging.debug(
        "executing function as function ==============> "+threading.currentThread().user)
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
    logging.debug("exiting function ==============> "+func.__name__)

# https://towardsdatascience.com/using-wrappers-to-log-in-python-ccffe4c46b54
