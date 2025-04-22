import time
import os
from celery import Celery

broker_url = os.environ.get("CELERY_BROKER_URL", "amqp://guest:guest@rabbitmq:5672//")
celery_app = Celery('tasks', broker=broker_url)

print("**BROKER_URL**", broker_url)

@celery_app.task
def generate_report():
    time.sleep(10)
    return "Report complete!"
