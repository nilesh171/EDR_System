import psutil
import time
import socket
import requests
from datetime import datetime

SERVER_URL = "http://127.0.0.1:8000/logs"
ENDPOINT_ID = socket.gethostname()
INTERVAL = 30  # seconds


def collect_process_telemetry():
    """
    Collects Windows process telemetry safely.
    """
    processes = []

    for proc in psutil.process_iter([
        "pid",
        "name",
        "exe",
        "ppid",
        "username",
        "cpu_percent",
        "memory_percent"
    ]):
        try:
            processes.append({
                "pid": proc.info["pid"],
                "name": proc.info["name"],
                "exe": proc.info["exe"],
                "ppid": proc.info["ppid"],
                "username": proc.info["username"],
                "cpu_percent": proc.info["cpu_percent"],
                "memory_percent": proc.info["memory_percent"]
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return processes


def send_telemetry():
    payload = {
        "endpoint_id": ENDPOINT_ID,
        "timestamp": datetime.utcnow().isoformat(),
        "processes": collect_process_telemetry()
    }

    try:
        requests.post(SERVER_URL, json=payload, timeout=5)
    except requests.exceptions.RequestException:
        pass  # Agent must never crash


if __name__ == "__main__":
    while True:
        send_telemetry()
        time.sleep(INTERVAL)
