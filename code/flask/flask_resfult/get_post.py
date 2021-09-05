from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

my_store = {}
my_store["gaurav"] = "gaurav"
my_store["gaurav1"] = "gaurav1"


class Student(Resource):
    def get(self, name):
        for student in my_store:
            if my_store[student] == name:
                return {"name": name}
        return {"message": "not found"}, 404

    def post(self, name):
        my_store[name] = name  # fetching from url is not good, for now just doing it
        return {"message": "created"}, 201


api.add_resource(Student, "/student/<string:name>", methods=["GET", "POST"])


if __name__ == "__main__":
    app.run(debug=True)
