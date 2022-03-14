from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.route("/api/test", methods=["GET"])
    def sample_route():
        return jsonify({"message": "This is a sample route"})

    @app.route("/api/hello", methods=["GET"])
    def hello_route():
        return jsonify({"message": "hello world"})

    return app
