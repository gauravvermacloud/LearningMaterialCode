from functools import wraps
import inspect
import threading
import logging
from flask import jsonify

# https://stackoverflow.com/questions/30904486/python-wrapper-function-taking-arguments-inside-decorator

# https://towardsdatascience.com/using-wrappers-to-log-in-python-ccffe4c46b54
