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
import Scheduler
import time
from flask_cors import CORS
from my_logger import wrap
from gevent import pywsgi
from OpenSSL import SSL


app = Flask(__name__)
app.register_blueprint(account_api)
cors = CORS(app, resources={r"/*": {"origins": config_reader.cors}})


@app.route('/api/test', methods=["GET"])
@wrap()
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


@ app.errorhandler(MyBaseException.MyBaseException)
def handle_not_found(e):
    return jsonify({"exception": "NotFound"}), 404


@ app.errorhandler(MyDerivedException.DerivedException)
def handle_bad_request(e):
    return jsonify({"exception": "Bad Request"}), 400


if __name__ == "__main__":
    if(config_reader.server == "Flask"):  
        app.run(
            debug=config_reader.debug,
            host=config_reader.host,
            port=config_reader.port
        )
    if(config_reader.server == "Waitress"):
        serve(app, host=config_reader.host,
              port=config_reader.port
              )
    if(config_reader.server == "Gevent"):
        #pip3 install gevent
        #https://serverfault.com/questions/224122/what-is-crt-and-key-files-and-how-to-generate-them
        #openssl genrsa 2048 > host.key
        #chmod 400 host.key
        #openssl req -new -x509 -nodes -sha256 -days 365 -key host.key -out host.cert
        server = pywsgi.WSGIServer(('0.0.0.0', 5000), app, 
                                   keyfile='host.key', 
                                   certfile='host.cert')
        server.serve_forever()
    

# To run with gunicorn ->>>>>  gunicorn --bind 0.0.0.0:5000 app:app
# To run with mod_wsgi ->>>>>>>>> mod_wsgi-express start-server app.py --processes 4

# https://flask.palletsprojects.com/en/2.2.x/deploying/mod_wsgi/
# https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
# https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-to-setup-Nginx-reverse-proxy-servers-by-example

# nginx
# https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/
# http://nginx.org/en/docs/http/load_balancing.html

# https://dev.to/thetrebelcc/how-to-run-a-flask-app-over-https-using-waitress-and-nginx-2020-235c
