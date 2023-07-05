# -*- coding: utf-8 -*-
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EMAILService:

    def on_post(self, request, response):
        receiver_address = request.media['receiver_address']
        mail_content = request.media['mail_content']

        sender_address = os.environ['SENDER_EMAIL']
        sender_pass = os.environ['SENDER_PASSWORD']

        message = MIMEMultipart()
        message['From'] = 'sangeet@finverv.com'
        message['To'] = receiver_address
        message['Subject'] = request.media['mail_subject']

        message.attach(MIMEText(mail_content, 'plain'))

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        try:
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            response.media = {'msg': f'Email sent to {receiver_address} successfully'}

        except ValueError:
            response.media = {'msg': 'Failed to send email'}
