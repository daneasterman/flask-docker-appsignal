import time
from celery import Celery

celery_app = Celery('tasks', broker='amqp://guest:guest@rabbitmq:5672//')

@celery_app.task
def generate_report():
    time.sleep(10)
    return "Report complete!"
