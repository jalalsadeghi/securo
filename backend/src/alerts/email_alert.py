from aiosmtplib import SMTP
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
EMAIL_FROM = os.getenv("EMAIL_FROM")

async def send_alert_email(email_to: str, subject: str, content: str):
    message = EmailMessage()
    message["From"] = EMAIL_FROM
    message["To"] = email_to
    message["Subject"] = subject
    message.set_content(content)

    smtp = SMTP(hostname=SMTP_HOST, port=SMTP_PORT, start_tls=True)
    await smtp.connect()
    await smtp.login(SMTP_USER, SMTP_PASS)
    await smtp.send_message(message)
    await smtp.quit()
