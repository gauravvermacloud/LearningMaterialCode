from asyncio import exceptions
import json
from lib2to3.pytree import Base
from flask import Blueprint, jsonify
from apis.exceptions import MyBaseException, MyDerivedException
from my_logger import wrap
import threading


account_api = Blueprint('account_api', __name__)


@account_api.route("/account")
@wrap()
def account_list():
    current_thrd = threading.currentThread()
    print(current_thrd.ident)
    print(current_thrd.my_prop)
    return jsonify([1, 2, 3, 4])


@account_api.route("/account/id")
def account_by_id():
    return jsonify({"id": 1})


@account_api.route("/raise_baise")
def raise_base_exception():
    raise MyBaseException.MyBaseException


@account_api.route("/raise_derived")
def raise_derived_exception():
    raise MyDerivedException.DerivedException