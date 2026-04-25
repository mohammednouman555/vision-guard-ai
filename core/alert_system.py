import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from datetime import datetime
import os

# 🔐 Configure these
EMAIL = "mohdnouman555@gmail.com"
PASSWORD = "uvee ctcv nbsk akhm"   # Gmail App Password (NOT normal password)
TO_EMAIL = "mohdnouman555@gmail.com"


def send_alert(image_path=None):
    try:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        msg = MIMEMultipart()
        msg["Subject"] = "🚨 Intruder Alert - VisionGuard AI"
        msg["From"] = EMAIL
        msg["To"] = TO_EMAIL

        body = f"""
Intruder detected!

Time: {time_now}

Please check your system immediately.
"""
        msg.attach(MIMEText(body, "plain"))

        # 📸 Attach image if available
        if image_path and os.path.exists(image_path):
            with open(image_path, "rb") as f:
                img = MIMEImage(f.read())
                img.add_header(
                    "Content-Disposition",
                    "attachment",
                    filename=os.path.basename(image_path),
                )
                msg.attach(img)
        else:
            print("⚠️ No image attached (file not found or path empty)")

        # 📩 Send email
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
        server.quit()

        print("📩 Email sent successfully")

    except Exception as e:
        print("❌ Email error:", e)