from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


class Student(Resource):
    def get(self, name):
        return {"name": name}


api.add_resource(HelloWorld, "/")
api.add_resource(Student, "/student/<string:name>", methods=["GET"])


if __name__ == "__main__":
    app.run(debug=True)
