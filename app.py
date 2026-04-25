from flask import Flask, render_template, jsonify, Response
import threading
import time
import cv2
import os
from datetime import datetime

from core.camera import start_camera, stop_camera
from core.intrusion_detector import detect_intrusion
from core.face_recognition_module import load_known_faces
from core.alert_system import send_alert
from core.system_lock import lock_system
from core.logger import log_event, get_logs

app = Flask(__name__)

monitoring = False
camera_thread = None
cap = None
latest_frame = None
last_status = "IDLE"


def run_security():
    global monitoring, cap, latest_frame, last_status

    os.makedirs("data/intruders", exist_ok=True)

    cap = start_camera()
    if cap is None:
        return

    last_intruder_time = 0  # 🔥 cooldown control

    while monitoring:
        ret, frame = cap.read()
        if not ret:
            continue

        status, faces = detect_intrusion(frame)
        last_status = status

        # 🔥 Draw bounding boxes
        for (top, right, bottom, left) in faces:
            top *= 2
            right *= 2
            bottom *= 2
            left *= 2

            color = (0, 255, 0) if status == "AUTHORIZED" else (0, 0, 255)

            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, status, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        latest_frame = frame.copy()

        # 🚨 Intruder handling (safe)
        if status == "INTRUDER":
            current_time = time.time()

            # ⛔ Prevent spam (10 sec gap)
            if current_time - last_intruder_time > 10:
                last_intruder_time = current_time

                # 📸 Save image
                filename = datetime.now().strftime("intruder_%Y%m%d_%H%M%S.jpg")
                path = os.path.join("data/intruders", filename)

                cv2.imwrite(path, frame)
                print(f"📸 Intruder image saved: {path}")

                log_event("Intruder detected")

                # 📩 Send email with image
                send_alert(path)

                # 🔒 Lock system
                lock_system()

        elif status == "AUTHORIZED":
            log_event("Authorized access")

        time.sleep(0.2)

    stop_camera()


def generate_frames():
    global latest_frame

    while True:
        if latest_frame is None:
            continue

        _, buffer = cv2.imencode('.jpg', latest_frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/start", methods=["POST"])
def start():
    global monitoring, camera_thread

    if not monitoring:
        monitoring = True
        camera_thread = threading.Thread(target=run_security, daemon=True)
        camera_thread.start()

    return jsonify({"status": "started"})


@app.route("/stop", methods=["POST"])
def stop():
    global monitoring
    monitoring = False
    return jsonify({"status": "stopped"})


@app.route("/status")
def status():
    return jsonify({
        "monitoring": monitoring,
        "detection": last_status
    })


@app.route("/logs")
def logs():
    return jsonify({"logs": get_logs()})


if __name__ == "__main__":
    load_known_faces()
    print("🔐 System Ready...")

    # 🔥 IMPORTANT: prevents crash / multiple threads
    app.run(debug=True, use_reloader=False)