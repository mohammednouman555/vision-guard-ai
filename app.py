from flask import Flask, render_template, Response, jsonify
import cv2
import threading
import time
import os

from core.camera import start_camera
from core.intrusion_detector import detect_intrusion
from core.face_recognition_module import load_known_faces
from core.logger import log_event
from core.alert_system import send_alert
from core.system_lock import lock_system

app = Flask(__name__)

camera = start_camera()
load_known_faces()

last_alert_time = 0
latest_status = "Monitoring..."


@app.route("/")
def home():
    return render_template("index.html")


# 🔴 Live camera feed
def generate_frames():
    while True:
        ret, frame = camera.read()
        if not ret:
            continue

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route("/video_feed")
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# 📜 Get logs
@app.route("/logs")
def get_logs():
    if not os.path.exists("data/logs.txt"):
        return jsonify([])

    with open("data/logs.txt", "r") as f:
        lines = f.readlines()

    return jsonify(lines[-10:])  # last 10 logs


# 📸 Get latest intruder image
@app.route("/intruder")
def get_intruder():
    path = "data/intruders/intruder.jpg"
    if os.path.exists(path):
        return path
    return ""


# 🔴 Get status
@app.route("/status")
def get_status():
    return jsonify({"status": latest_status})


def run_security():
    global last_alert_time, latest_status

    print("🔐 VisionGuard AI started...")

    while True:
        ret, frame = camera.read()

        if not ret:
            continue

        result = detect_intrusion(frame)

        if result == "INTRUDER":
            current_time = time.time()

            if current_time - last_alert_time > 10:
                latest_status = "🚨 Intruder Detected"

                img_path = "data/intruders/intruder.jpg"
                cv2.imwrite(img_path, frame)

                send_alert(img_path)
                lock_system()
                log_event("Intruder detected")

                last_alert_time = current_time
        else:
            latest_status = "✅ Authorized User"

        cv2.imshow("VisionGuard AI", frame)

        if cv2.waitKey(1) == 27:
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    t = threading.Thread(target=run_security)
    t.start()

    app.run(debug=True)