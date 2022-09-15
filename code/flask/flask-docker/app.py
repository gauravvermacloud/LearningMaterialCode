from flask import Flask, jsonify
from apis.account_api import account_api

app = Flask(__name__)
app.register_blueprint(account_api)


@app.route('/api/test', methods=["GET"])
def method_name():
    print("Before Return")
    return jsonify({"key": "1Value1"})


if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )
