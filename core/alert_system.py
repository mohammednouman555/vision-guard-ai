import smtplib
from email.message import EmailMessage
import config

def send_alert(image_path):
    try:
        msg = EmailMessage()
        msg['Subject'] = "🚨 Intruder Detected!"
        msg['From'] = config.EMAIL
        msg['To'] = config.RECEIVER_EMAIL

        msg.set_content("Unauthorized access detected!")

        with open(image_path, 'rb') as f:
            img_data = f.read()
            msg.add_attachment(img_data, maintype='image', subtype='jpeg', filename="intruder.jpg")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(config.EMAIL, config.PASSWORD)
            smtp.send_message(msg)

        print("📩 Alert sent!")

    except Exception as e:
        print("❌ Email failed:", e)