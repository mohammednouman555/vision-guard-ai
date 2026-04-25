import cv2
import face_recognition
from core.face_recognition_module import known_face_encodings

unknown_counter = 0
UNKNOWN_THRESHOLD = 5
TOLERANCE = 0.5


def detect_intrusion(frame):
    global unknown_counter

    small = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

    faces = face_recognition.face_locations(rgb)

    if len(faces) == 0:
        unknown_counter = 0
        return "NO_FACE", []

    encodings = face_recognition.face_encodings(rgb, faces)

    results = []

    for encoding in encodings:
        matches = face_recognition.compare_faces(
            known_face_encodings, encoding, tolerance=TOLERANCE
        )

        if True in matches:
            unknown_counter = 0
            results.append("AUTHORIZED")
        else:
            unknown_counter += 1

            if unknown_counter >= UNKNOWN_THRESHOLD:
                unknown_counter = 0
                results.append("INTRUDER")
            else:
                results.append("PROCESSING")

    return results[0], faces