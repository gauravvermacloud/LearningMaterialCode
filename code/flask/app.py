from Emp import Emp
from flask import Flask
from flask import jsonify
from Emp import Emp 

app = Flask (__name__)

my_emp = Emp(name="x",age=5)

@app.route('/')
def get():
    return jsonify({'a':1, 'b':2})

@app.route('/emp')
def get_emp_by_id():
    return jsonify(my_emp)

@app.route('/<id>')
def get_by_id(id):
    return jsonify({id:1})


app.run(port=8080)