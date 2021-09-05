from flask import Flask
from flask import request, make_response
from flask import jsonify

app = Flask (__name__)


store = {
            "my_store":{
                            "name": "my_store",
                            "items":{
                                        "item_1":25.00,
                                        "item_2":30.00
                                    }
                       }
        }

#Post /store -->data--> {name:}
@app.route('/store', methods=['POST'])
def create_store():
    input_request_json = request.get_json()
    store_name = input_request_json.get('name')
    store[store_name] = {"name":store_name}
    json_store = __get_store_by_name__(store_name)
    return make_response(jsonify(json_store),201)


#Get /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    return jsonify(__get_store_by_name__(name))



def __get_store_by_name__(name):
    this_store = store[name]
    return this_store

#Get /store
@app.route('/store', methods=['GET'])
def get_all_stores():
    return jsonify(store)

#Post /store/<string:name>/item --> data--> {item:price}
@app.route('/store/<string:store_name>/item', methods = ['POST'])
def add_item_to_store(store_name):
    store = __get_store_by_name__(store_name)
    request_json = request.get_json()
    item_name = request_json['item_name']
    item_price = request_json['item_price']
    store['items'][item_name] = item_price
    return jsonify(store)


#Get /store/<String:name>/item
@app.route('/store/<string:store_name>/item/<string:item_name>', methods=['GET'])
def get_item_from_store(store_name, item_name):
    store = __get_store_by_name__(store_name)
    item = store['items'][item_name]
    return jsonify(item)


app.run(port=8086)