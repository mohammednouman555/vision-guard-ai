import face_recognition
import os

KNOWN_ENCODINGS = []
KNOWN_NAMES = []


def load_known_faces():
    global KNOWN_ENCODINGS, KNOWN_NAMES
    path = "data/authorized_faces"

    for file in os.listdir(path):
        img_path = os.path.join(path, file)

        img = face_recognition.load_image_file(img_path)
        encodings = face_recognition.face_encodings(img)

        if len(encodings) == 0:
            print(f"⚠️ No face found in {file}, skipping...")
            continue

        KNOWN_ENCODINGS.append(encodings[0])
        KNOWN_NAMES.append(file.split(".")[0])

    print(f"✅ Loaded {len(KNOWN_ENCODINGS)} authorized faces")


def recognize_face(frame):
    rgb = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb)

    if len(face_locations) == 0:
        return False

    encodings = face_recognition.face_encodings(rgb, face_locations)

    for encoding in encodings:
        matches = face_recognition.compare_faces(KNOWN_ENCODINGS, encoding)

        if True in matches:
            return True

    return False