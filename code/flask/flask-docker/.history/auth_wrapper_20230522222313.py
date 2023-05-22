from functools import wraps

import threading


def auth_dec(roles=['Annnonymous']):
    def somedec_inner(*args, **kwargs):
        # do stuff with somearg, someopt, args and kwargs
        print(roles)
        print(threading.currentThread().user)
        response = fn(*args, **kwargs)
        return response
    return somedec_inner

# https://stackoverflow.com/questions/30904486/python-wrapper-function-taking-arguments-inside-decorator

# https://towardsdatascience.com/using-wrappers-to-log-in-python-ccffe4c46b54
