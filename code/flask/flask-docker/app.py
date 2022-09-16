from distutils.command.config import config
from distutils.log import debug
from flask import Flask, jsonify
from apis.account_api import account_api
import threading
import _threading_local
from flask import request
from apis.exceptions import MyBaseException, MyDerivedException
import config_reader
from waitress import serve

app = Flask(__name__)
app.register_blueprint(account_api)


@app.route('/api/test', methods=["GET"])
def method_name():
    print("Before Return -1")

    current_thrd = threading.currentThread()
    print(current_thrd.ident)
    print(current_thrd.my_prop)

    return jsonify({"key": "1Value1"})


@app.before_request
def before_request():
    current_thrd = threading.currentThread()
    print(current_thrd.ident)
    current_thrd.my_prop = "Test"
    print(current_thrd.my_prop)


@app.errorhandler(MyBaseException.MyBaseException)
def handle_not_found(e):
    return jsonify({"exception": "NotFound"}), 404


@app.errorhandler(MyDerivedException.DerivedException)
def handle_bad_request(e):
    return jsonify({"exception": "Bad Request"}), 400


if __name__ == "__main__":
    if(config_reader.server == "Flask"):
        app.run(
            debug=config_reader.debug,
            host=config_reader.host,
            port=config_reader.port
        )
    else:
        serve(app, host=config_reader.host,
              port=config_reader.port)
