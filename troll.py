
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from random import choice
# pip install pyleetspeak
_ = load_dotenv()


def send_email(to, subject, message):

    email_address = os.environ.get("EMAIL_ADDRESS")
    email_password = os.environ.get("EMAIL_PASSWORD")

    # create email
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = to
    msg.set_content(message)

    # send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

msg = 'sensies'
message_mod = ''.join(choice((str.upper, str.lower))(c) for c in msg)

