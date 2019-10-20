from celery import Celery, bootsteps
from kombu import Consumer, Exchange, Queue
import time

my_queue = Queue('custom', Exchange('custom'), routing_key='route_key')

app = Celery(broker='amqp://')


class MyConsumerStep(bootsteps.ConsumerStep):

    def get_consumers(self, channel):
        return [Consumer(
            channel, queues=[my_queue], callbacks=[self.handle_messages],
            accept=['json']
        )]

    def handle_messages(self, body, message):
        print('Recieved Message : {0!r}', format(body))
        message.ack()


app.steps['consumer'].add(MyConsumerStep)




# celery -A consumer worker --loglevel=info
