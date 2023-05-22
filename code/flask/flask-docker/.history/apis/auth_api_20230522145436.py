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
def login():
    body = request.get_json()
    logging.debug("Object received for authentication = "+str(body))
    # We need to make it into a class and not work with json and throw exception if the object is not proper and handle it
    authenticate = Authenticate().from_json(body)
    return jsonify(body)