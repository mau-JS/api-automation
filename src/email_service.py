import smtplib
import os
import logging
from email.message import EmailMessage
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

load_dotenv()

def send_mail(address,subject,body):
    sender = os.getenv("EMAIL_USER")
    password = os.getenv("APP_PASSWORD")
    host = os.getenv("EMAIL_HOST")
    port = int(os.getenv("EMAIL_PORT", 587))
    message = EmailMessage()
    message["From"] = sender
    message["To"] = address
    message["Subject"] = subject
    message.set_content(body)

    with smtplib.SMTP(host, port) as smtp:
        smtp.starttls()
        smtp.login(sender, password)
        smtp.send_message(message)
    logger.info("Email sent successfully to %s", address)