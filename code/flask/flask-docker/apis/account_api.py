from asyncio import exceptions
import json
from lib2to3.pytree import Base
from flask import Blueprint, jsonify
from apis.exceptions import MyBaseException, MyDerivedException

account_api = Blueprint('account_api', __name__)


@account_api.route("/account")
def account_list():
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
