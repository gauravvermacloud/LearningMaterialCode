import configparser
config = configparser.ConfigParser()
config.read("config.ini")

port = int(config["Default"]["port"])

host = config["Default"]["host"]


debug = True

if (config["Default"]["Debug"] == "False"):
    debug = False

server = config["Default"]["Server"]

cors = config["Default"]["cors"]

is_scheduler_enabled = True

if (config["Default"]["is_scheduler_enabled"] == "False"):
    is_scheduler_enabled = False

is_ssl_enabled = False
if (config["Default"]["is_ssl_enabled"] == "True"):
    is_ssl_enabled = True