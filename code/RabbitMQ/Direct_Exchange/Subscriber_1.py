# This subscriber listens to all the messages
# debug warn fatel

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='DirectExhange', exchange_type='direct')

# Create a queue and let the Message broker decide the queue name
result = channel.queue_declare(queue='', exclusive=True)

# Get the name of the queue created
queue_name = result.method.queue

channel.queue_bind(exchange='DirectExhange',
                   queue=queue_name, routing_key="debug")
channel.queue_bind(exchange='DirectExhange',
                   queue=queue_name, routing_key="warn")
channel.queue_bind(exchange='DirectExhange',
                   queue=queue_name, routing_key="fatel")


def callback(ch, method, properties, body):
    print(method.routing_key + " ====> " + str(body)


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
