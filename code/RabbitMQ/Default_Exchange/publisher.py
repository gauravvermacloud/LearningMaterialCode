import constants
import pika
import time

# Create a server connection with given address
connection = pika.BlockingConnection(
    pika.ConnectionParameters(constants.SERVER_ADDRESS))

# Based on connection create a channel
channel = connection.channel()

# Create a queue if needed and define the queue . This will be the queue where messages will be published
channel.queue_declare(constants.QUEUE_NAME)

# while there is no intrupt publish a message every 10 seconds

message_number = 0
while(True):
    channel.basic_publish(
        exchange=constants.DEFAULT_EXCHANGE_NAME, routing_key=constants.QUEUE_NAME, body=constants.SAMPLE_MESSAGE_FORMAT.format(message_number))
    message_number = message_number+1
    # wait for 5 seconds
    time.sleep(constants.SLEEP_TIME)

connection.close()
