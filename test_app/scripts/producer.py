from celery import Celery, bootsteps
from kombu import Consumer, Exchange, Queue
import time

my_queue = Queue('custom', Exchange('custom'), routing_key='route_key')

app = Celery(broker='amqp://')


def send_me_a_message(who, producer=None):
    with app.producer_or_acquire(producer) as producer:
        producer.publish(
            {'hello': who},
            serializer='json',
            exchange=my_queue.exchange,
            routing_key=my_queue.routing_key,
            declare=[my_queue],
            retry=True,
        )


if __name__ == '__main__':
    while True:
        send_me_a_message('world!')
