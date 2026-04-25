import cv2

camera = None

def start_camera():
    global camera

    # 🔥 FIX: Use CAP_MSMF (works on most Windows systems)
    camera = cv2.VideoCapture(0, cv2.CAP_MSMF)

    if not camera.isOpened():
        print("❌ Camera not accessible")
        return None

    print("📷 Camera started")
    return camera


def stop_camera():
    global camera
    if camera:
        camera.release()
        camera = None
        print("🛑 Camera stopped")