import os
import socket
from flask import Flask, jsonify
from tasks import generate_report
app = Flask(__name__)
from dotenv import load_dotenv
load_dotenv()

env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route('/start-task/')
def start_task():
    print("📬 /start-task was called!")

    # ✅ DNS resolution test
    try:
        rabbitmq_ip = socket.gethostbyname("rabbitmq")
        print(f"✅ DNS OK: rabbitmq resolves to {rabbitmq_ip}")
    except Exception as e:
        print(f"❌ DNS FAIL: rabbitmq not resolving — {e}")
        return jsonify({"error": "rabbitmq DNS resolution failed"}), 500

    # ✅ Port connectivity test
    try:
        sock = socket.create_connection(("rabbitmq", 5672), timeout=5)
        print("✅ Port OK: Connected to rabbitmq:5672")
        sock.close()
    except Exception as e:
        print(f"❌ PORT FAIL: Cannot connect to rabbitmq:5672 — {e}")
        return jsonify({"error": "rabbitmq port 5672 unreachable"}), 500

    # ✅ If both tests passed, send task
    task = generate_report.delay()
    return jsonify({"task_id": task.id, "status": "started"}), 202

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)