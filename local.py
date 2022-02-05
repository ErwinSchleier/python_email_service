import smtplib
from email.mime.text import MIMEText

sender = 'admin@example.com'
receivers = ['info@example.com']

port = 1024
msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = sender
msg['To'] = receivers[0]

with smtplib.SMTP('localhost', port) as server:
    server.sendmail(sender, receivers, msg.as_string())
    print("Successfully sent email")