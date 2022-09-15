import json
from flask import Blueprint, jsonify
account_api = Blueprint('account_api', __name__)


@account_api.route("/account")
def account_list():
    return jsonify([1, 2, 3, 4])
