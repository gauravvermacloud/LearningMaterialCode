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

# Now we do not want a collision in queue names
# To ensure we are using a unique queue name each time

queue = channel.queue_declare(queue='', exclusive=True)

# Now pull out the name of the queue from the actual queue

queue_name = queue.method.queue

# Now bind the queue to exchange
print("binding to queue = " + queue_name)

channel.queue_bind(exchange=constants.EXCHANGE_NAME,
                   queue=queue_name)

channel.basic_consume(
    queue=queue_name, on_message_callback=call_back, auto_ack=True)

channel.start_consuming()
