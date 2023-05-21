from asyncio import exceptions
import json
from lib2to3.pytree import Base
from flask import Blueprint, jsonify
from apis.exceptions import MyBaseException, MyDerivedException
from my_logger import wrap
import threading
import logging


# https://auth0.com/blog/how-to-handle-jwt-in-python/

auth_api = Blueprint('auth_api', __name__)


@auth_api.route("/authenticate")
@wrap()
@app.@app.route('/login', methods=['POST'])
def method_name():
    body = request.get_json()
    logging.debug("Object received for authentication = "+)
