import pika
import time
import constants

# Create a server connection with given address
connection = pika.BlockingConnection(
    pika.ConnectionParameters(constants.SERVER_ADDRESS))

# Based on connection create a channel
channel = connection.channel()

# Now create a fanout exchange
channel.exchange_declare(
    exchange=constants.EXCHANGE_NAME, exchange_type='fanout')

# now start publishing the messages, we will see in fanout case messages are published to all queues

message_number = 0
while(True):
    channel.basic_publish(
        exchange=constants.EXCHANGE_NAME, routing_key='', body=constants.SAMPLE_MESSAGE_FORMAT.format(message_number))

    print("published ==> "+constants.SAMPLE_MESSAGE_FORMAT.format(message_number))

    message_number = message_number+1
    # wait for 5 seconds
    time.sleep(constants.SLEEP_TIME)

connection.close()
