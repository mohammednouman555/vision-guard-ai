import os
from datetime import datetime

LOG_FILE = "data/logs.txt"

def log_event(message):
    os.makedirs("data", exist_ok=True)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as f:
        f.write(f"[{now}] {message}\n")


def get_logs():
    if not os.path.exists(LOG_FILE):
        return []

    with open(LOG_FILE, "r") as f:
        return f.readlines()[-20:]