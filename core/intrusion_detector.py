from core.face_recognition_module import recognize_face

def detect_intrusion(frame):
    try:
        authorized = recognize_face(frame)

        if authorized:
            return "AUTHORIZED"
        else:
            return "INTRUDER"

    except Exception as e:
        print("Error:", e)
        return "AUTHORIZED"