from asyncio import exceptions
import json
from lib2to3.pytree import Base
from flask import Blueprint, jsonify
from apis.exceptions import MyBaseException, MyDerivedException
from my_logger import wrap
import threading
import logging

auth_api = Blueprint('auth_api', __name__)


@account_api.route("/authenticate")
@wrap()
def login():
    pass
