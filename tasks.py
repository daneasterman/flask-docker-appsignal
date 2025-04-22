import time
import os
from celery import Celery
from dotenv import load_dotenv
load_dotenv()

import functools
print = functools.partial(print, flush=True)

broker_url = os.environ.get("CELERY_BROKER_URL", "amqp://guest:guest@rabbitmq:5672//")
celery_app = Celery('tasks', broker=broker_url)

@celery_app.task
def ping():
    print("👋 ping task received")
    return "pong"

@celery_app.task
def generate_report():
    print("📊 STARTING generate_report task")
    time.sleep(5)
    print("✅ FINISHED generate_report task")
    return "Report complete!"