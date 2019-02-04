import json
import os

from app import app
from flask_mail import Mail, Message


mail = Mail(app)

with open(os.path.abspath(os.path.join('app/config/config.json', ))) as f:
    config = json.load(f)


def send_mail(email, password):
    with mail.connect() as conn:
        message = ('Hello, you have been invited to upjob system. Here is '
                   'your password: {}.'.format(password))
        subject = 'Invitation for upjob system'
        msg = Message(sender=config['MAIL_USERNAME'], recipients=[email],
                      body=message, subject=subject)
        conn.send(msg)
