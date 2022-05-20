# This publisher, publishes messages of type
# debug,fatel to exchange
import pika

# Create a connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# Create a connection
channel = connection.channel()

# Create an exchange
channel.exchange_declare(exchange='DirectExhange', exchange_type='direct')

message_id = 1
routing_keys = ['debug', 'fatel']
while(True):
    message = "Message "+str(message_id)
    key_id = message_id % 2

    key = routing_keys[key_id]
    print("Publishing Message " + message + " to key "+key)

    channel.basic_publish(exchange='DirectExhange',
                          routing_key=key, body=message)
    message_id = message_id+1
