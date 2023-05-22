from functools import wraps

import threading


# https://realpython.com/primer-on-python-decorators/
# Check link aboove may be it explains why only first function is decorated

def auth_dec(roles=['Annnonymous']):
    def decorate(func):
        """ Decorator """
        def call(*args, **kwargs):
            print(roles)
            result = func(*args, **kwargs)
            return result
        return call
    return decorate

# https://stackoverflow.com/questions/30904486/python-wrapper-function-taking-arguments-inside-decorator

# https://towardsdatascience.com/using-wrappers-to-log-in-python-ccffe4c46b54
# https://realpython.com/primer-on-python-decorators/
