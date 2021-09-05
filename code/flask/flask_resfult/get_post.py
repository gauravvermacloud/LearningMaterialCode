# import flask, Resource api etc
from flask import Flask
from flask_restful import Resource, Api

# Create app and api
app = Flask(__name__)
api = Api(app)

# Temp data store
my_store = {}
my_store["gaurav"] = "gaurav"
my_store["gaurav1"] = "gaurav1"


# Class to handle resource
class Student(Resource):
    # Note the name is get and post for the methods
    def get(self, name):
        for student in my_store:
            if my_store[student] == name:
                return {"name": name}  # This by default will be the json + 200
        return {"message": "not found"}, 404  # Or we can have an explict source

    def post(self, name):
        my_store[name] = name  # fetching from url is not good, for now just doing it
        return {"message": "created"}, 201


# We just add the url and methods it will work with
api.add_resource(Student, "/student/<string:name>", methods=["GET", "POST"])


if __name__ == "__main__":
    app.run(debug=True)
