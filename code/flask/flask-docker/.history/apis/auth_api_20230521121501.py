from asyncio import exceptions
import json
from lib2to3.pytree import Base
from flask import Blueprint, jsonify, request
from apis.exceptions import MyBaseException, MyDerivedException
from my_logger import wrap
import threading
import logging


# https://auth0.com/blog/how-to-handle-jwt-in-python/

auth_api = Blueprint('auth_api', __name__)


@auth_api.route("/authenticate")
@wrap()
@auth_api.route('/authenticate/login', methods=['POST'])
def method_name():
    body = request.get_json()
    logging.debug("Object received for authentication = "+body)
    return jsonify(body)
