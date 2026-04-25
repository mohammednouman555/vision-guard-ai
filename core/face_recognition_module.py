import face_recognition
import os

# 🔥 GLOBAL STORAGE (IMPORTANT)
known_face_encodings = []
known_face_names = []


def load_known_faces():
    global known_face_encodings, known_face_names

    path = "data/authorized_faces"

    for file in os.listdir(path):
        img_path = os.path.join(path, file)

        try:
            image = face_recognition.load_image_file(img_path)
            encodings = face_recognition.face_encodings(image)

            if len(encodings) == 0:
                print(f"⚠️ No face found in {file}, skipping...")
                continue

            known_face_encodings.append(encodings[0])
            known_face_names.append(file.split(".")[0])

        except Exception as e:
            print(f"Error loading {file}: {e}")

    print(f"✅ Loaded {len(known_face_encodings)} authorized faces")