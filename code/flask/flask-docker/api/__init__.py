from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.route('/api/test', methods=["GET"])
    def method_name():
        print("Before Return")
        return jsonify({"key": "1Value1"})
    return app
