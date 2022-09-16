import configparser
config = configparser.ConfigParser()
config.read("config.ini")

port = int(config["Default"]["port"])

host = config["Default"]["host"]


debug = True

if (config["Default"]["Debug"] == "False"):
    debug = False

server = config["Default"]["Server"]
