import os
import socket
from flask import Flask, jsonify
from tasks import generate_report
app = Flask(__name__)

env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route('/start-task/')
def start_task():
    print("📬 /start-task was called!")
    task = generate_report.delay()
    print("RabbitMQ IP:", socket.gethostbyname("rabbitmq"))
    return jsonify({"task_id": task.id, "status": "started"}), 202

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)