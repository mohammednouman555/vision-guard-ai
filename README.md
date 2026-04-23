---

# 🛡️ VisionGuard AI — Smart Anti-Theft & Intrusion Detection System


---

## 📌 Overview

VisionGuard AI is an intelligent laptop security system that uses computer vision and AI-based face recognition to detect unauthorized access in real time.
It continuously monitors the user through the webcam and automatically takes security actions when an intruder is detected.

---

## 🚨 Problem Statement

Laptops contain sensitive personal and professional data but remain vulnerable when left unattended in places like hostels, libraries, or workplaces.
Traditional security methods such as passwords are passive and cannot detect or respond to unauthorized physical access in real time.

---

## 💡 Solution

VisionGuard AI provides an active security layer by:

- Monitoring the user via webcam
- Identifying authorized vs unauthorized users
- Triggering real-time responses like alerts, system lock, and evidence capture

---

## 🔄 How It Works

1. 📷 Camera Monitoring
   Continuously checks for presence of a person

2. 🧠 Face Recognition
   Compares detected face with authorized user dataset

3. 🚨 Intrusion Detection
   If face does not match → marked as intruder

4. ⚡ Automatic Actions
   
   - 📸 Capture intruder image
   - 📩 Send email alert
   - 🔒 Lock the system
   - 📝 Save logs

5. 📊 Dashboard
   
   - Live camera feed
   - System status
   - Intruder images
   - Logs

---

## ✨ Features

- 🎥 Real-time webcam monitoring
- 🧠 Face recognition authentication
- 🚨 Intrusion detection system
- 📸 Evidence capture (image)
- 📩 Email alert with attachment
- 🔒 Automatic system lock
- 📜 Activity logging
- 📊 Live dashboard interface
- ⏱️ Cooldown mechanism (prevents repeated alerts)

---

## 🛠️ Technologies Used

- Python
- Flask
- OpenCV
- face_recognition (dlib-based)
- NumPy
- HTML, CSS, JavaScript

---

## 📂 Project Structure
```
VisionGuardAI/
│
├── app.py
├── config.py
├── requirements.txt
│
├── core/
│   ├── camera.py
│   ├── intrusion_detector.py
│   ├── face_recognition_module.py
│   ├── alert_system.py
│   ├── system_lock.py
│   ├── logger.py
│
├── data/
│   ├── authorized_faces/
│   ├── intruders/
│   └── logs.txt
│
├── templates/
│   └── index.html
```
---

## ⚙️ Setup Instructions

1️⃣ Clone Repository

- git clone https://github.com/your-username/VisionGuardAI.git
- cd VisionGuardAI

---

2️⃣ Create Virtual Environment

- python -m venv venv
- venv\Scripts\activate

---

3️⃣ Install Dependencies

- pip install -r requirements.txt

---

4️⃣ Add Authorized Face

- Place your image in:

- data/authorized_faces/

Example:

- nouman.jpg

---

5️⃣ Configure Email Alerts

- Edit "config.py":
 
EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"
RECEIVER_EMAIL = "your_email@gmail.com"

⚠️ Use Gmail App Password, not your normal password.

---

6️⃣ Run the Project

- python app.py

---

7️⃣ Open Dashboard

- http://127.0.0.1:5000

---

## 📊 Dashboard Features

- 🎥 Live camera feed
- 📊 Real-time system status
- 📸 Intruder image preview
- 📜 Activity logs

---

## 🎯 Use Cases

- 🏫 College / Hostel security
- 🏢 Office data protection
- ☕ Public places (cafes, libraries)
- 🧑‍💻 Personal privacy protection
- 📝 Online exam monitoring

---

## 🚀 Future Scope

- 📱 Mobile app integration
- 🌍 Geo-location tracking
- 🔔 Push notifications
- 🧠 Confidence score display
- ☁️ Cloud-based monitoring system

---

## 🔐 Why This is Cybersecurity

VisionGuard AI performs:

- Detection → Identifies unauthorized users
- Prevention → Locks system
- Response → Sends alerts & captures evidence
- Logging → Maintains activity records

---

## 👨‍💻 Author

Mohammed Nouman

---

## ⭐ Acknowledgment

This project demonstrates how AI and computer vision can be used to build real-time security systems for everyday devices.

---

## 📌 Note

This is a prototype system designed for educational and demonstration purposes.
---
