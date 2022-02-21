import constants
import pika


def call_back(channel, method, properties, body):
    print(body)


# Create a server connection with given address
connection = pika.BlockingConnection(
    pika.ConnectionParameters(constants.SERVER_ADDRESS))

# Based on connection create a channel
channel = connection.channel()

# Now create a fanout exchange
channel.exchange_declare(
    exchange=constants.EXCHANGE_NAME, exchange_type='fanout')

# Create a queue if needed and define the queue . This will be the queue where messages will be published
channel.queue_declare(constants.QUEUE_NAME)


# bind the queue to callback
channel.basic_consume(queue=constants.QUEUE_NAME,
                      on_message_callback=call_back, auto_ack=True)

# Now start consuming messages
channel.start_consuming()
